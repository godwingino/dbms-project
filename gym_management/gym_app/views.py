from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from .models import *




# Create your views here.

def home(request, pk):
    customer = customers.objects.get(username=pk)
    return render(request,'gym_app/dasboard.html', {'customer': customer})
    
def contact(request):
    return render(request,'gym_app/contact.html')

# def login(request):
#     return render(request,'gym_app/login.html')

def product(request):
    return HttpResponse('product')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            auth_login(request, form.get_user())
            return redirect('home')  # Redirect to the desired page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'gym_app/login.html', {'form': form})
