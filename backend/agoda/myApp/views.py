from django.shortcuts import render ,redirect
# Create your views here.


def index(request):

    context={}

    return render(request,"citys.html",context,)


def endyearPage(request):
    
    context={}
    
    return render(request, "endyear.html" ,context)



def eliteoffersPage(request):
    
    context={}
    
    return render(request, "eliteoffers.html", context)



def paylessPage(request):
    
    context={}
    
    return render(request, "payless.html", context)



def staylongerPage(request):
    
    context={}
    
    return render(request, "staylonger.html", context)



def dealsPage(request):
    
    context={}
    
    return render(request, "deals.html", context)



def reservationPage(request):
    
    context={}
    
    return render(request, "reservation.html", context)



def chancePage(request):

    context={}
    
    return render(request, "chance.html", context)