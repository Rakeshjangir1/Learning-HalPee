from django.shortcuts import render, redirect
from django.contrib import messages

#Importing Models Here
from .models.users import user_registration
# Create your views here.


def login(request):
    return render(request, 'loginpage.html')

def signup(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Last_Name = request.POST.get('last_name')
        Phone_Number = request.POST.get('phone_number')
        Email = request.POST.get('email').casefold()
        Password = request.POST.get('password')
        if user_registration.objects.filter(Email=Email).exists():
            messages.warning(request, f'Hi {Name.upper()} this Email is already in used')
            return redirect('/signup')
        else:
            registeration = user_registration(Name=Name,Last_Name=Last_Name,Phone_number=Phone_Number,Email=Email,password=Password)
            registeration.save()
    return render(request, 'signuppage.html')
