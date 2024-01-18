from django.shortcuts import render ,redirect,get_object_or_404
from.models import*

from AppUser.models import*

from django.contrib import messages
from django.core.paginator import Paginator

def index(request):
    city=City.objects.all()
    context={
        "city":city,
    }
    return render(request,"index.html",context)

def city(request,Cityİd):
    city=City.objects.get(id=Cityİd)
    hotels = hotel.objects.filter(city=city)

    hotel_data = []
    for h in hotels:
        imgs = AdditionalImage.objects.filter(hotels=h)
        comments = comment.objects.filter(hotelscom=h).order_by("-date").first()
        hotel_data.append({"hotel": h, "images": imgs, "latest_comments": comments})

    context = {"hotel_data": hotel_data ,"city":city}
    
    return render(request, "citys.html", context)





def detail(request,Cardid):

    hotels=hotel.objects.get(id=Cardid)
    imgs = AdditionalImage.objects.filter(hotels=hotels)
    comments=comment.objects.filter(hotelscom=hotels)
  


    
    if request.method=="POST":
        button=request.POST.get("button")
        if button=="comment":

           name=request.POST.get("name")
           email=request.POST.get("email")
           title=request.POST.get("title")
           text=request.POST.get("text")
           date=request.POST.get("date")
           rating=request.POST.get("rating")
           com=comment(user=request.user,hotelscom=hotels,title=title,email=email,text=text,date=date,   rating=rating)
           com.save()
        elif button=="reservation":
            person=request.POST.get("person")
            dates=request.POST.get("date")
            

            if hotels.discounted_price is not None and hotels.discounted_price > 0:
               total_price = int(person) * hotels.discounted_price
            else:
              total_price = int(person) * hotels.price
            bask = baskets(user=request.userinfos, hotel=hotels, total_price=total_price ,date=dates)
            bask.save()
            
    context = {"hotels": hotels ,"imgs":imgs ,"comments":comments }

    return render(request,"detay.html",context,)



# def endyearPage(request,Couponİd):
    
#      hotels = hotel.objects.get()
    
    
#      hotel_data = []
#      for h in hotels:
#         imgs = AdditionalImage.objects.filter(hotels=h)
#         hotel_data.append({"hotel": h, "images": imgs})

#      context = {"hotel_data": hotel_data}
    
#      return render(request, "endyear.html", context)  
def endyearPage(request, ):
    # Tıklanan kuponun id'sine göre kupon nesnesini al

    # Kupon indirim oranından yüksek veya eşit olan otelleri getir
    hotels = hotel.objects.all()

    hotel_data = []
    for h in hotels:
        imgs = AdditionalImage.objects.filter(hotels=h)
        hotel_data.append({"hotel": h, "images": imgs})

    context = {"hotel_data": hotel_data, }
    
    return render(request, "endyear.html", context)
