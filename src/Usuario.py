import unittest

class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña, fecha_creacion, estado, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.fecha_creacion = fecha_creacion
        self.estado = estado
        self.categoria = categoria

    def Crear_cuenta(self):
        return "Cuenta creada exitosamente"

    def Iniciar_sesion(self):
        if self.estado == "inactivo":
            return "Error: Usuario inactivo"
        return "Inicio de sesión exitoso"

    def Cambiar_contraseña(self, correo, contraseña_actual, nueva_contraseña):
        if self.correo != correo:
            return "Error: Usuario no registrado"
        if self.contraseña != contraseña_actual:
            return "Error: Contraseña actual incorrecta"
        if len(nueva_contraseña) > 320:
            return "Error: Contraseña demasiado larga"
        self.contraseña = nueva_contraseña
        return "Contraseña cambiada correctamente"

    def crear_tarea(self):
        return "Tarea creada exitosamente"

    def Editar_tarea(self):
        return "Tarea editada exitosamente"

    def Eliminar_tarea(self):
        return "Tarea eliminada exitosamente"
