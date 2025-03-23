import unittest
from src.Usuario import Usuario

class TestCrearCuenta(unittest.TestCase):
    def setUp(self):
        """Inicialización de usuarios registrados"""
        self.usuarios_registrados = {}

    def test_crear_cuenta_correctamente(self):
        usuario = Usuario("Alejandro", "Pérez", "alejo@example.com", "StrongPass123", "2025-03-07", "Activo", "General")
        self.usuarios_registrados[usuario.correo] = usuario
        self.assertIn("alejo@example.com", self.usuarios_registrados)

    def test_crear_cuenta_y_iniciar_sesion(self):
        usuario = Usuario("Laura", "Gómez", "laura@example.com", "SecurePass456", "2025-03-07", "Activo", "General")
        self.usuarios_registrados[usuario.correo] = usuario
        resultado = "Registro e inicio exitoso" if usuario.correo in self.usuarios_registrados else "Error al iniciar sesión"
        self.assertEqual(resultado, "Registro e inicio exitoso")

    def test_crear_cuenta_con_correo_alternativo(self):
        usuario = Usuario("Carlos", "Rodríguez", "carlos123@example.com", "AnotherPass789", "2025-03-07", "Activo", "General")
        self.usuarios_registrados[usuario.correo] = usuario
        self.assertIn("carlos123@example.com", self.usuarios_registrados)

    def test_crear_cuenta_con_contraseña_muy_larga(self):
        contraseña_larga = "A" * 101
        with self.assertRaises(ValueError):
            Usuario("María", "Fernández", "maria@example.com", contraseña_larga, "2025-03-07", "Activo", "General")

    def test_crear_cuenta_con_nombre_muy_largo(self):
        nombre_largo = "A" * 51
        with self.assertRaises(ValueError):
            Usuario(nombre_largo, "Ramírez", "ramirez@example.com", "SecurePass123", "2025-03-07", "Activo", "General")

    def test_crear_cuenta_con_correo_ya_registrado(self):
        usuario1 = Usuario("Sofía", "López", "sofia@example.com", "SecurePass123", "2025-03-07", "Activo", "General")
        self.usuarios_registrados[usuario1.correo] = usuario1
        with self.assertRaises(ValueError):
            Usuario("Sofía", "López", "sofia@example.com", "SecurePass123", "2025-03-07", "Activo", "General")

    def test_crear_cuenta_con_contraseña_debil(self):
        with self.assertRaises(ValueError):
            Usuario("Diego", "Torres", "diego@example.com", "123", "2025-03-07", "Activo", "General")

    def test_crear_cuenta_con_datos_incompletos(self):
        with self.assertRaises(ValueError):
            Usuario("", "Muñoz", "munoz@example.com", "SecurePass123", "2025-03-07", "Activo", "General")

if __name__ == '__main__':
    unittest.main()

