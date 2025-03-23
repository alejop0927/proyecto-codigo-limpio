from mi_app.models import Usuario
from mi_app.models import Tarea
from mi_app.models import UsuTarea


def Crear_cuenta(nombre,apellido,correo,contraseña):
    if Usuario.objects.filter(correo=correo).exists():
        return "Error: El correo ya esta registrado"
    else:
        usuario= Usuario.objects.create(nombre=nombre,apellido=apellido,correo=correo,contraseña=contraseña)
        usuario.set_password(contraseña)
        usuario.save()
        return f"Usuario {usuario.nombre} fue creado exitosamente"
        

def Cambiar_contraseña(correo, nueva_contraseña=None):
    try:  
         usuario=Usuario.objects.get(correo=correo)
         usuario.set_password(nueva_contraseña)
         usuario.save()
         return "contraseña cambaida exitosamente"    
    
    except Usuario.DoesNotExist:
        return "Error: Usuario no encontrado"
    

def Iniciar_sesion(correo, contraseña):
    usuario=Usuario.objects.filter(correo=correo).first()

    if not usuario:
        return "El usuario no exite"
    
    if not usuario.check_password(contraseña):
        return "contraseña incorrecta"
    
    return "Inicio de sesion correcto"
      

def crear_tarea(nombre_tarea,texto_tarea,categoria,estado):
    if Tarea.objects.filter(nombre_tarea=nombre_tarea).exists():
        return "Error: ya existe una tarea con ese nombre"
    else:
       tarea=Tarea.objects.create(nombre_tarea=nombre_tarea,texto_tarea=texto_tarea,categoria=categoria,estado=estado)
       return f"la terea con nombre : {tarea} fue creada con exito"

def Editar_tarea(nombre_tarea, nuevo_nombre_tarea, texto_tarea, categoria, estado):
    if Tarea.objects.filter(nombre_tarea=nombre_tarea).exists():
        tarea_editada = Tarea.objects.get(nombre_tarea=nombre_tarea)  
        tarea_editada.nombre_tarea = nuevo_nombre_tarea  
        tarea_editada.texto_tarea = texto_tarea  
        tarea_editada.categoria = categoria  
        tarea_editada.estado = estado  
        tarea_editada.save()  
        return tarea_editada  
    else:
        return None  


def Eliminar_tarea(nombre_tarea, nuevo_nombre_tarea, texto_tarea, categoria, estado):
    if Tarea.objects.filter(nombre_tarea=nombre_tarea).exists():
        tarea_a_eliminar=Tarea.objects.get(nombre_tarea=nombre_tarea)
        tarea_a_eliminar.delete()
        return f"la tarea con nombre {tarea_a_eliminar} fue eliminada con exito"
    else:
        return "la tarea no existe"
       


