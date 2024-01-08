from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User



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
        password2=request.POST.get("password2")

        if not User.objects.filter(email=email).exists():
            user=User.objects.create_user()
        else:
             messages.error(request,"bu email zaten kullanılıyor")

        
        
    context={}

    return render(request,"user/register.html",context)