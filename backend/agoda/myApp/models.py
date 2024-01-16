from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

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
    discount=models.IntegerField(("İndirim Oranı"),max_length=5,blank=True,null=True)
    star=models.IntegerField(("Otel Yıldızı"),null=True,blank=True)
    content = RichTextField(null=True,blank=True)
   
    def average_rating(self):
        comments = comment.objects.filter(hotelscom=self)
        if comments:
            total_rating = sum(comment.rating for comment in comments)
            return total_rating / len(comments)
        return None
    @property
    def discounted_price(self):
        if self.price is not None and self.discount is not None:
            return self.price - (self.price * (self.discount / 100))
        return None
    def __str__(self):
        return self.hotelname


    
class AdditionalImage(models.Model):
    hotels=models.ForeignKey(hotel, verbose_name=("oteller"),on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='additional_images',max_length=50,null=False,blank=False)


class comment(models.Model):
    user=models.ForeignKey(User, verbose_name=("yorum yapan kullanıcı Kullanıcı"),on_delete=models.CASCADE,null=True)
    hotelscom=models.ForeignKey(hotel, verbose_name=("otel yorumu"), on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(("Yorum başlık"), max_length=50,null=True,blank=True)
    email=models.CharField(("email"), max_length=50,null=True,blank=True)
    text=models.TextField(("yorum"),max_length=500,null=True,blank=True)
    date=models.DateField(("tarih"), auto_now=False, auto_now_add=False,null=True,blank=True)
    rating = models.DecimalField("Değerlendirme Puanı", max_digits=3, decimal_places=1, 
    validators=[MaxValueValidator(10)], null=True, blank=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the average rating for the associated hotel after saving a new comment
        hotel = self.hotelscom
        hotel.rating = hotel.average_rating()
        hotel.save()

