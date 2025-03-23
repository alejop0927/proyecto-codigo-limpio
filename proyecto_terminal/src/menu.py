from .Usuario import Usuario
from .tarea import Tarea


def menu(usuario_id):
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Ver tareas")
        print("2. Crear tarea")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Cerrar sesión")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            Tarea.ver_tareas(usuario_id)
        elif opcion == "2":
            nombre = input("Nombre de la tarea: ")
            texto = input("Descripción: ")
            categoria = input("Categoría: ")
            estado = input("Estado (Pendiente/Completado): ")
            Tarea.crear_tarea(usuario_id, nombre, texto, categoria, estado)
        elif opcion == "3":
            tarea_id = input("ID de la tarea a editar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_texto = input("Nueva descripción: ")
            nueva_categoria = input("Nueva categoría: ")
            nuevo_estado = input("Nuevo estado: ")
            Tarea.editar_tarea(usuario_id, tarea_id, nuevo_nombre, nuevo_texto, nueva_categoria, nuevo_estado)
        elif opcion == "4":
            tarea_id = input("ID de la tarea a eliminar: ")
            Tarea.eliminar_tarea(usuario_id, tarea_id)
        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

def inicio():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        print("4. Cambiar contraseña")  
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            usuario_id = Usuario.iniciar_sesion(correo, contraseña)  
            if usuario_id:
                menu(usuario_id)
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            Usuario.registrar(nombre, apellido, correo, contraseña)
        elif opcion == "3":
            print("Saliendo...")
            break
        elif opcion == "4":  
            correo = input("Correo: ")
            contraseña = input("Coloque su nueva contraseña: ")
            nueva_contraseña = contraseña
            resultado = Usuario.cambiar_contraseña(correo, nueva_contraseña)
            print(resultado)
        else:
            print("Opción inválida, intenta de nuevo.")

inicio()
