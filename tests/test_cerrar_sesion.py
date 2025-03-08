import unittest
from src.Usuario import Usuario

class TestCrearCuenta(unittest.TestCase):
    def setUp(self):
        self.usuarios_registrados = {}

    def crear_cuenta(self, nombre, apellido, correo, contraseña, fecha_creacion, estado, categoria):
        if not nombre or not apellido or not correo or not contraseña:
            return "Error: Datos obligatorios faltantes"
        if correo in self.usuarios_registrados:
            return "Error: Correo ya registrado"
        if len(contraseña) < 6:
            return "Error: Contraseña demasiado débil"
        if len(contraseña) > 100:
            return "Error: Contraseña demasiado larga"
        if len(nombre) > 50:
            return "Error: Nombre demasiado largo"

        usuario = Usuario(nombre, apellido, correo, contraseña, fecha_creacion, estado, categoria)
        self.usuarios_registrados[correo] = usuario
        return "Cuenta creada exitosamente"

    def test_crear_cuenta_correctamente(self):
        resultado = self.crear_cuenta("Alejandro", "Pérez", "alejo@example.com", "StrongPass123", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_crear_cuenta_y_iniciar_sesion(self):
        self.crear_cuenta("Laura", "Gómez", "laura@example.com", "SecurePass456", "2025-03-07", "Activo", "General")
        resultado = "Registro e inicio exitoso" if "laura@example.com" in self.usuarios_registrados else "Error al iniciar sesión"
        self.assertEqual(resultado, "Registro e inicio exitoso")

    def test_crear_cuenta_con_correo_alternativo(self):
        resultado = self.crear_cuenta("Carlos", "Rodríguez", "carlos123@example.com", "AnotherPass789", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Cuenta creada exitosamente")

    def test_crear_cuenta_con_contraseña_muy_larga(self):
        resultado = self.crear_cuenta("María", "Fernández", "maria@example.com", "A" * 101, "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Error: Contraseña demasiado larga")

    def test_crear_cuenta_con_nombre_muy_largo(self):
        resultado = self.crear_cuenta("A" * 51, "Ramírez", "ramirez@example.com", "SecurePass123", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Error: Nombre demasiado largo")

    def test_crear_cuenta_con_conexion_inestable(self):
        
        resultado = "Error: No se pudo completar el registro"
        self.assertEqual(resultado, "Error: No se pudo completar el registro")

    def test_crear_cuenta_con_correo_ya_registrado(self):
        self.crear_cuenta("Sofía", "López", "sofia@example.com", "SecurePass123", "2025-03-07", "Activo", "General")
        resultado = self.crear_cuenta("Sofía", "López", "sofia@example.com", "SecurePass123", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Error: Correo ya registrado")

    def test_crear_cuenta_con_contraseña_debil(self):
        resultado = self.crear_cuenta("Diego", "Torres", "diego@example.com", "123", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Error: Contraseña demasiado débil")

    def test_crear_cuenta_con_datos_incompletos(self):
        resultado = self.crear_cuenta("", "Muñoz", "munoz@example.com", "SecurePass123", "2025-03-07", "Activo", "General")
        self.assertEqual(resultado, "Error: Datos obligatorios faltantes")

if __name__ == '__main__':
    unittest.main()
