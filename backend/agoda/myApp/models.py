from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class hotel(models.Model):
    mainimg=models.ImageField(("Anaresim"),upload_to="Anaresim",  max_length=None, blank=True,null=False )
    hotelname=models.CharField(("Otel adı"), max_length=50,null=True,blank=True)
    hoteltitle=models.TextField(("Otel başlık"),max_length=500,null=True,blank=True)
    hotellocation=models.CharField(("Otel adresi"), max_length=50,null=True,blank=True)
    hotellocationmap=models.CharField(("Otel Konumu"), max_length=50,null=True,blank=True)
    hotellocationmapbox=models.TextField(("Otel Konumu kutu"), max_length=500,null=True,blank=True)
    rating = models.DecimalField("Değerlendirme Puanı", max_digits=5, decimal_places=2, null=True, blank=True)
    price=models.IntegerField(("Otel Fiyatı"),null=True,blank=True)
    star=models.IntegerField(("Otel Yıldızı"),null=True,blank=True)
    content = RichTextField(null=True,blank=True)
    def __str__(self) :
        return self.hotelname

    
class AdditionalImage(models.Model):
    hotels=models.ForeignKey(hotel, verbose_name=("oteller"),on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='additional_images',max_length=50,null=False,blank=False)