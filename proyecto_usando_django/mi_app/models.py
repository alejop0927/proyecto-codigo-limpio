from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150, blank=True, null=True)
    correo = models.EmailField(max_length=250, unique=True)

    USERNAME_FIELD = 'correo' 
    REQUIRED_FIELDS = ['nombre']  

    class Meta:
        db_table = 'login'

class Tarea(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Completada'),
    ]

    id_tarea = models.AutoField(primary_key=True)
    nombre_tarea = models.CharField(max_length=250, blank=True, null=True)
    texto_tarea = models.CharField(max_length=250, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='Pendiente')

    class Meta:
        db_table = 'tarea'

class UsuTarea(models.Model):
    id_usu_tarea = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario', related_name='tareas_asignadas')
    id_tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, db_column='id_tarea', related_name='usuarios_asignados')

    class Meta:
        db_table = 'usu_tarea'
