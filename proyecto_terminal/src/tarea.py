from src.config import conectar_bd

class Tarea:
    @staticmethod
    def crear_tarea(id_usuario, nombre_tarea, texto_tarea, categoria, estado):
        conn = conectar_bd()
        if conn:
            cursor = conn.cursor()

   
            cursor.execute(
                "INSERT INTO tarea (nombre_tarea, texto_tarea, categoria, estado) VALUES (%s, %s, %s, %s)",
                (nombre_tarea, texto_tarea, categoria, estado)
            )
            id_tarea = cursor.lastrowid  

            
            cursor.execute(
                "INSERT INTO usu_tarea (id_tarea, id_usuario) VALUES (%s, %s)",
                (id_tarea, id_usuario)
            )

            conn.commit()
            print(f"Tarea '{nombre_tarea}' creada con éxito y asignada al usuario {id_usuario}")

            cursor.close()
            conn.close()

    @staticmethod
    def ver_tareas(id_usuario):
        conn = conectar_bd()
        if conn:
            cursor = conn.cursor()

           
            cursor.execute("""
                SELECT t.id_tarea, t.nombre_tarea, t.texto_tarea, t.categoria, t.estado
                FROM tarea t
                INNER JOIN usu_tarea ut ON t.id_tarea = ut.id_tarea
                WHERE ut.id_usuario = %s
            """, (id_usuario,))
            
            tareas = cursor.fetchall()
            cursor.close()
            conn.close()

            if tareas:
                print("\nTus tareas:")
                for tarea in tareas:
                    print(f"{tarea[0]}. {tarea[1]} - {tarea[3]} ({tarea[4]})\n    {tarea[2]}")
            else:
                print("No tienes tareas registradas.")

    @staticmethod
    def editar_tarea(id_usuario, id_tarea, nuevo_nombre, nuevo_texto, nueva_categoria, nuevo_estado):
        conn = conectar_bd()
        if conn:
            cursor = conn.cursor()

           
            cursor.execute(
                "SELECT id_tarea FROM usu_tarea WHERE id_tarea = %s AND id_usuario = %s",
                (id_tarea, id_usuario)
            )
            if not cursor.fetchone():
                print("Error: No puedes modificar esta tarea")
                cursor.close()
                conn.close()
                return

           
            cursor.execute(
                "UPDATE tarea SET nombre_tarea = %s, texto_tarea = %s, categoria = %s, estado = %s WHERE id_tarea = %s",
                (nuevo_nombre, nuevo_texto, nueva_categoria, nuevo_estado, id_tarea)
            )
            conn.commit()
            print("Tarea actualizada correctamente")

            cursor.close()
            conn.close()

    @staticmethod
    def eliminar_tarea(id_usuario, id_tarea):
        conn = conectar_bd()
        if conn:
            cursor = conn.cursor()

            
            cursor.execute(
                "SELECT id_tarea FROM usu_tarea WHERE id_tarea = %s AND id_usuario = %s",
                (id_tarea, id_usuario)
            )
            if not cursor.fetchone():
                print("Error: No puedes eliminar esta tarea")
                cursor.close()
                conn.close()
                return

           
            cursor.execute("DELETE FROM usu_tarea WHERE id_tarea = %s AND id_usuario = %s", (id_tarea, id_usuario))

           
            cursor.execute("SELECT id_tarea FROM usu_tarea WHERE id_tarea = %s", (id_tarea,))
            if not cursor.fetchone():
              
                cursor.execute("DELETE FROM tarea WHERE id_tarea = %s", (id_tarea,))

            conn.commit()
            print("Tarea eliminada correctamente")

            cursor.close()
            conn.close()
