from django.db import models
from myApp.models import *
from django.contrib.auth.models import User


# Create your models here.

class userinfo(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"),on_delete=models.CASCADE,null=True)
    name=models.CharField(("isim"),null=True,blank=True,max_length=20)
    surname=models.CharField(("soy isim"),null=True,blank=True,max_length=20)
    email=models.CharField(("email"),null=True,blank=True,max_length=50)
    phone=models.CharField(("telefon numarası"), max_length=11, null=True, blank=True)
    password=models.CharField(("şifre"), max_length=50)
    def __str__(self) :
        return self.user.username


class baskets(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    hotel=models.ForeignKey(hotel, verbose_name=("hotel"), on_delete=models.CASCADE)
    total_price=models.IntegerField(("Toplam fiyat"),max_length=11, null=True, blank=True)
    date=models.DateField(("Tarih"), auto_now=False, auto_now_add=False,max_length=11, null=True, blank=True)
    person=models.IntegerField(("Kişi sayısı" ),max_length=20, null=True, blank=True)

class Deletereservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(hotel, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    date = models.DateField()
    person = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.hotel.hotelname} - {self.date}"
