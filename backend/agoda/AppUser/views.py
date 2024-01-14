from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import *



# kullanıcı girişini bu fonksiyon sayesinde hem email hemde telefon ile giriş yapıyor
def custom_authenticate(request, *, email=None, phone=None, password=None):
    try:
        if email:
            user_info = userinfo.objects.get(email=email, password=password)
        elif phone:
            user_info = userinfo.objects.get(phone=phone, password=password)
        else:
            return None

        user = user_info.user
        return user
    except userinfo.DoesNotExist:
        return None



def login_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        button=request.POST.get("button")
        if button=="email":
            user = custom_authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request,user)
                return redirect("/city")
            else:
                hata="Kullanıcı adı yada şifre hatalı"
                context={"hata":hata}
                return render(request,"user/login.html",context)
        elif button=="mobil":
            user = custom_authenticate(request,phone=phone,password=password)
         
            if user is not None:
                login(request,user)
                return redirect("/city")
            else:
                hata="Telefon Numarası yada şifre hatalı"
                context={"hata":hata}
                return render(request,"user/login.html",context)


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


def userProfile(request):
    user=User.objects.get(id=request.user.id)
    userinfos=userinfo.objects.get(user=user)

    if request.method=="POST":
        name=request.POST.get("name")
        surname=request.POST.get("surname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")

        user.first_name=name
        user.last_name=surname
        user.email=email
        user.set_password(password)
        userinfos.name=name
        userinfos.surname=surname
        userinfos.email=email
        userinfos.phone=phone
        userinfos.password=password
        user.save()
        userinfos.save()
        login(request,user)

        return redirect("userprofile")
    context={"userinfos":userinfos,}

    return render(request,"user/userprofile.html",context)