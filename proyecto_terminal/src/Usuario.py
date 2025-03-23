from src.config import conectar_bd

class Usuario:
    @staticmethod
    def registrar(nombre, apellido, correo, contraseña):
        conn = conectar_bd()
        if not conn:
            print("Error al conectar con la base de datos")
            return None

        try:
            cursor = conn.cursor()

           
            cursor.execute("SELECT id_usuario FROM login WHERE correo = %s", (correo,))
            if cursor.fetchone():
                print("Error: El correo ya está registrado")
                return None

            
            cursor.execute(
                "INSERT INTO login (nombre, apellido, correo, contraseña) VALUES (%s, %s, %s, %s)",
                (nombre, apellido, correo, contraseña)
            )
            conn.commit()
            print(f"Usuario {nombre} registrado exitosamente")
        except Exception as e:
            print(f"Error al registrar usuario: {e}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def iniciar_sesion(correo, contraseña):
        conn = conectar_bd()
        if not conn:
            print("Error al conectar con la base de datos")
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario FROM login WHERE correo = %s AND contraseña = %s", (correo, contraseña))
            usuario = cursor.fetchone()
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            usuario = None
        finally:
            cursor.close()
            conn.close()

        if usuario:
            print("Inicio de sesión exitoso")
            return usuario[0]
        else:
            print("Correo o contraseña incorrectos")
            return None

    @staticmethod
    def cambiar_contraseña(correo, nueva_contraseña):
        conn = conectar_bd()
        if not conn:
            return "Error al conectar con la base de datos"

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id_usuario FROM login WHERE correo = %s", (correo,))
            usuario = cursor.fetchone()

            if usuario:
                id_usuario = usuario[0]
                cursor.execute("UPDATE login SET contraseña = %s WHERE id_usuario = %s", (nueva_contraseña, id_usuario))
                conn.commit()
                return "Contraseña cambiada exitosamente"
            else:
                return "Error: Usuario no encontrado"
        except Exception as e:
            return f"Error al actualizar contraseña: {e}"
        finally:
            cursor.close()
            conn.close()
