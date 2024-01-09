from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *



# Create your views here.


def login(request):
    context={}

    return render(request,"user/login.html",context)
def register(request):

    if request.method=="POST":
        name=request.POST.get("name")
        surname=request.POST.get("surname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password1=request.POST.get("password1")

        if not User.objects.filter(email=email).exists():
          if not userinfo.objects.filter(phone=phone) :
             user=User.objects.create_user(
                 first_name=name,
                 last_name=surname,
                 password=password1,
                 email=email,
                 username=name,
             )
             user.save()
             userinfos=userinfo(
                 user=user,
                 name=name,
                 surname=surname,
                 email=email,
                 phone=phone,
                 password=password1
             )
             userinfos.save()
             
             return redirect("login")
          else:
              messages.error(request,"bu numara zaten kullanılıyor")
        else:
             messages.error(request,"bu email zaten kullanılıyor")

        
        
    context={}

    return render(request,"user/register.html",context)