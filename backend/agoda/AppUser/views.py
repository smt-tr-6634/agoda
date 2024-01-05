from django.shortcuts import render

# Create your views here.


def login(request):
    context={}

    return render(request,"user/login.html",context)
def register(request):
    context={}

    return render(request,"user/register.html",context)