from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'index.html')


# Create your views here.
def register(request):
    form=UserCreationForm
    if request.method == 'POST':
        regform=UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request, 'User has been registered.')

    return render(request,'registration/register.html',{'form':form})