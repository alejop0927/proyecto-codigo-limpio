from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register, password_change

urlpatterns = [
    path('register/', register, name='register'),
    
    # Cambio de contraseña personalizado
    path('password_change/', password_change, name='password_change'),

    # Página de éxito después de cambiar la contraseña
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='mi_app/password_change_done.html'
    ), name='password_change_done'),
]
