from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from mi_app.views import register
from mi_app.views import password_change
from django.contrib.auth import views as auth_views

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'register.html')

urlpatterns = [
    path('admin/', admin.site.urls),      
    path('', dashboard, name='dashboard'),  
    path('register/', register, name='register'),
    path('password_change/', password_change, name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='mi_app/password_change_done.html'
    ), name='password_change_done'),
]


