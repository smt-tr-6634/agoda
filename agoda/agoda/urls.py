"""agoda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp.views import*
from AppUser.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("city/<Cityİd>",city,name="city"),
    path("login/",login_user,name="login"),
    path("register/",register,name="register"),
    path("endyear/", endyearPage, name="endyear"),
    path("", index, name="index"),
    path("detay/<Cardid>",detail,name="detay"),
    path("userprofile/",userProfile,name="userprofile"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cancel_reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('delete_comment/<int:comid>/', delete_comments, name='delete_comments'),
    path("logout/",logoutuser,name="logoutuser"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
