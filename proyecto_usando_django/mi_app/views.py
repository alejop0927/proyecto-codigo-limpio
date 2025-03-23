from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def dashboard(request):
    return render(request, 'mi_app/dashboard.html')  

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  
    else:
        form = UserCreationForm()
    
    return render(request, "mi_app/register.html", {"form": form})


def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantiene la sesión activa después del cambio de contraseña
            return redirect("password_change_done")  
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, "password_change.html", {"form": form})
