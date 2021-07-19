"""interviewproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from interviewapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homeview,name="home"),
    path('question/', views.showquestions,name="questionlist"),
    path('questionadd/' , views.questionaddform,name='qadd'),
    path('topic/<int:pk>' , views.gettopic,name="gtopic"),
    path('signup/',views.signup,name="signup"),
    path('signin/' , views.signin,name="signin"),
    path('logout/', views.signout,name="signout"),
    path('gethandle/' , views.gethandle,name="gethandle"),
    path('solvedcount/' , views.questionsolvedinfo,name="solvedcount"),
    path('addexp/' , views.addexperience,name="addexp"),
    path('showcomp/' , views.showcompany,name="showexp"),
    path('viewexp/<int:pk>' , views.viewexperience,name="viewexp")
]
