from django.contrib import admin
from django.urls import path,include
# from donation.views import
from django.conf.urls.static import static
from . import settings
from django.shortcuts import render, redirect

urlpatterns = [
    path('admin/',admin.site.urls),
    # path('',index,name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda r:redirect('home-view')),
    path('donation/', include('donation.urls')),
    path('templates/<str:tmp>', lambda req, tmp:render(req, tmp)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
