from django.urls import path
from.import views
urlpatterns=[
    path("",views.home,name='home'),
    path('account/register/',views.register,name='register')
]