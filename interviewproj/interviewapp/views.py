from django.shortcuts import render,redirect
from .models import question,topics,usertohandle,experience,company
from .forms import questionadd,queryhandle,experienceadd
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
import requests
import json
def showcompany(request):
    l1 = company.objects.all()
    return render(request,'interviewstuff/showcomp.html',{'list':l1})
def viewexperience(request,pk):
    comp = company.objects.filter(pk=pk)[0]
    list = experience.objects.filter(companyexp=comp).all()
    return render(request, 'interviewstuff/viewexp.html', {'list':list})

def addexperience(request):
    if(request.method=="POST"):
        form1 = experienceadd(request.POST)
        if(form1.is_valid()):
            cexp = form1.cleaned_data.get('companyexp')
            nameofperson1 = form1.cleaned_data.get('nameofperson')
            nameofcollege1 = form1.cleaned_data.get('nameofcollege')
            typeofrole1 = form1.cleaned_data.get('typeofrole')
            experience1 = form1.cleaned_data.get('experience')

            requiredcompany = company.objects.filter(company_name=cexp)[0]
            x1 = experience.objects.create(companyexp=requiredcompany,nameofperson=nameofperson1,nameofcollege=nameofcollege1,typeofrole=typeofrole1,experience=experience1)
            x1.save()
            return redirect('home')
        else:
            print("failed")
            return redirect('home')
    else:
        form1=experienceadd()
        return render(request,'interviewstuff/addexperience.html',{'form1':form1})



def homeview(request):
    return redirect('questionlist')
def showquestions(request):
    l1 = topics.objects.all()
    return render(request,'interviewstuff/questions.html',{'relevant':l1})
def gettopic(request,pk):
    ob = topics.objects.filter(id=pk)[0];
    val = question.objects.filter(qtopic=ob)
    return render(request,'interviewstuff/topic.html' , {'dict':val})
def questionsolvedinfo(request):
    h1 = usertohandle.objects.filter(user=request.user)[0]
    handle1 = h1.handle

    string1 = "https://codeforces.com/api/user.status?handle="+str(handle1)+"&from=1&count=10"
    dictprobs = {}
    listofquestions = question.objects.all()
    for quest in listofquestions:
        print(str(quest.contest)+str(quest.index))
        dictprobs[str(quest.contest)+str(quest.index)]=0

    print(handle1)
    response = requests.get(string1).text
    reqdict  = json.loads(response)
    resultlist = reqdict['result']
    #print(resultlist)
    ans1=0

    for items in resultlist:
        temp =  str(items['problem']['contestId'])+items['problem']['index']
        print(temp)
        if((temp in dictprobs) and dictprobs[temp]==0 and items['verdict']=="OK"):
            ans1=ans1+1
            dictprobs[temp]=1


    return render(request,'interviewstuff/questionsolved.html', {'num':ans1,'total':len(listofquestions)})


def gethandle(request):
    if(request.method=="POST"):
        form1 = queryhandle(request.POST)
        if(form1.is_valid()):
            han = form1.cleaned_data['handle']
            han1 = usertohandle.objects.create(user=request.user, handle=han)
            han1.save()
            return redirect('home')
        else:
            return redirect('home')
    else:
        form1= queryhandle()
        return render(request, 'interviewstuff/gethandle.html', {'form1':form1})


def questionaddform(request):
    form1=questionadd()
    if(request.method=="POST"):
        form2=questionadd(request.POST)

        if(form2.is_valid()):
            attr1=form2.cleaned_data.get('qname')
            attr2=form2.cleaned_data.get('qtype')
            attr3=form2.cleaned_data.get('qdescrip')
            attr4=form2.cleaned_data.get('qtopic')
            attr5 = form2.cleaned_data.get('qlink')
            #print(attr4)
            ob1=topics.objects.filter(topicname=attr4)[0]
            l=attr5.split('/')
            index1 = l[-1]
            contest1 = l[-2]
            x = question.objects.create(questionname=attr1,questiontype=attr2,questiondescription=attr3,qtopic=ob1,questionlink=attr5,index=index1,contest=contest1)
            x.save()

        return render(request,'interviewstuff/home.html')

    return render(request,'interviewstuff/qaddform.html',{'form':form1})
def signup(request):
    if(request.user.is_authenticated):
        return redirect('home')
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            form =UserCreationForm()
            return render(request,'interviewstuff/signup.html',{'form':form})
    else:
        form =UserCreationForm()
        return render(request,'interviewstuff/signup.html',{'form':form})

def signin(request):

    if(request.user.is_authenticated):
        return redirect('home')
    print("inside")
    if(request.method=="POST"):


        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if(user is not None):
            print("ok")
            login(request,user)
            return redirect('home')
        else:
            print ("not ok")
            return redirect('home')

    else:
        form =AuthenticationForm()
        return render(request,'interviewstuff/signin.html',{'form':form})
def signout(request):
    logout(request)
    return redirect('home')


# Create your views here.
