from django.db import models
from django.conf import settings
# Create your models here.
class topics(models.Model):
    topicname=models.CharField(max_length=255,blank=True,null=True);
    def __str__(self):
        return self.topicname
class question (models.Model):
    questionname = models.CharField(max_length=255,blank=True,null=True)
    questiontype = models.CharField(max_length=255)
    questiondescription = models.CharField(max_length=255)
    qtopic =models.ForeignKey(topics,on_delete=models.CASCADE,blank=True,null=True)
    questionlink = models.URLField(max_length=200,blank=True,null=True)
    index = models.CharField(max_length=255,blank=True,null=True)

    contest = models.CharField(max_length=255,blank=True,null=True)
    def __str__ (self):
        return self.questiontype
class usertohandle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete = models.CASCADE)
    handle = models.CharField(max_length=255,blank=True,null=True)
class company(models.Model):
    company_name = models.CharField(max_length=255)

class experience(models.Model):
    companyexp = models.ForeignKey(company,on_delete=models.CASCADE)
    nameofperson = models.CharField(max_length=255)
    nameofcollege = models.CharField(max_length=255)
    typeofrole = models.CharField(max_length=255)
    experience = models.CharField(max_length=2000,blank=True,null=True)
