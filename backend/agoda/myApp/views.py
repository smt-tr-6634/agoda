from django.shortcuts import render ,redirect
# Create your views here.


def index(request):

    context={}

    return render(request,"citys.html",context,)


def detail(request):
    context={}

    return render(request,"detay.html",context,)