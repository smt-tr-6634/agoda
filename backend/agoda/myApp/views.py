from django.shortcuts import render ,redirect
from.models import*
from django.contrib import messages

# Create your views here.

def city(request):
    hotels = hotel.objects.all()
    
    
    hotel_data = []
    for h in hotels:
        imgs = AdditionalImage.objects.filter(hotels=h)
        hotel_data.append({"hotel": h, "images": imgs})

    context = {"hotel_data": hotel_data}
    
    return render(request, "citys.html", context)


def detail(request,Cardid):

    hotels=hotel.objects.get(id=Cardid)
    imgs = AdditionalImage.objects.filter(hotels=hotels)
    
    context = {"hotels": hotels ,"imgs":imgs }

    return render(request,"detay.html",context,)



def endyearPage(request):
    
     hotels = hotel.objects.all()
    
    
     hotel_data = []
     for h in hotels:
        imgs = AdditionalImage.objects.filter(hotels=h)
        hotel_data.append({"hotel": h, "images": imgs})

     context = {"hotel_data": hotel_data}
    
     return render(request, "endyear.html", context)
    



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