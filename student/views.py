from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.shortcuts import redirect   
from django.contrib.auth.forms import UserCreationForm
from .models import User 

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            try:
                logged_user = User.objects.get(email=user_email)
                request.session['logged_user_id'] = logged_user.id
                return redirect('/home')
            except User.DoesNotExist:
                messages.error(request, "L'utilisateur avec cet email n'existe pas.")
                return redirect('login')
    else:
        form = AuthenticationForm()
    
    return render(request, 'student/registration/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request)
            messages.success(request, f"Coucou {username}, Votre compte a été créé avec succès !")
            return redirect("index")
    else:
        form = UserCreationForm()
    
    return render(request, "student/registration/register.html", {"form": form}) 


def logoutt ( request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')