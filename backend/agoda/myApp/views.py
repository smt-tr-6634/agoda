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