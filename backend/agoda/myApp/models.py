from django.db import models

# Create your models here.


class hotel(models.Model):
    mainimg=models.ImageField(("Anaresim"),upload_to="Anaresim",  max_length=None, blank=True,null=False )
    hotelname=models.CharField(("Otel adı"), max_length=50,null=True,blank=True)
    hotellocation=models.CharField(("Otel Konumu"), max_length=50,null=True,blank=True)
    rating=models.IntegerField(("Değerlendirme Puanı"),null=True,blank=True)
    price=models.IntegerField(("Otel Fiyatı"),null=True,blank=True)
    
    
class AdditionalImage(models.Model):
    image = models.ImageField(upload_to='additional_images',max_length=50,null=False,blank=False)
    hotels=models.ForeignKey(hotel, verbose_name=("oteller"), max_length=50,on_delete=models.CASCADE,null=False,blank=False)