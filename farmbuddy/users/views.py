
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Dataset

def home(request):
    return render (request,'users/home.html',{})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request,'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def Info(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        Dataset = Dataset.objects.filter(name__contains=searched)
     return render (request,'users/Info.html',{'searched': searched})

    else 
    return render (request,'users/Info.html',{})
