import mysql.connector


config = {
    'user': 'root',
    'password': 'A0927lejop#',
    'host': 'localhost',
    'database': 'project_codigo_limpio',
    'port': 3306
}


def conectar_bd():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
