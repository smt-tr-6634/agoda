from django.contrib import admin
from.models import *

# Register your models here.

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage

class CardAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageInline]

admin.site.register(hotel, CardAdmin)
admin.site.register(AdditionalImage)
admin.site.register(comment)