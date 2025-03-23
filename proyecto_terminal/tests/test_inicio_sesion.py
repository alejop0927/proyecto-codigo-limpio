import unittest
from src.Usuario import Usuario  

class TestInicioSesion(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        self.usuario = Usuario("Juan", "Pérez", "usuario@example.com", "contraseña_correcta", "2024-03-07", "activo", "normal")

    def test_inicio_sesion_correcto(self):
        """Debe permitir el inicio de sesión con credenciales correctas"""
        self.assertEqual(self.usuario.Iniciar_sesion(), "Inicio de sesión exitoso")

    def test_inicio_sesion_mayusculas(self):
        """Debe permitir el inicio de sesión aunque el correo esté en mayúsculas"""
        usuario_mayusculas = Usuario("Juan", "Pérez", "USUARIO@EXAMPLE.COM", "contraseña_correcta", "2024-03-07", "activo", "normal")
        self.assertEqual(usuario_mayusculas.Iniciar_sesion(), "Inicio de sesión exitoso")

    def test_inicio_sesion_despues_cerrar_sesion(self):
        """Debe permitir iniciar sesión nuevamente después de cerrar sesión"""
        self.usuario.cerrar_sesion()
        self.assertEqual(self.usuario.Iniciar_sesion(), "Inicio de sesión exitoso")

    def test_inicio_sesion_contraseña_larga(self):
        """Debe permitir el inicio de sesión con una contraseña larga"""
        contraseña_larga = "a" * 128
        usuario_largo = Usuario("Juan", "Pérez", "usuario@example.com", contraseña_larga, "2024-03-07", "activo", "normal")
        self.assertEqual(usuario_largo.Iniciar_sesion(), "Inicio de sesión exitoso")

    def test_inicio_sesion_correo_largo(self):
        """Debe manejar correos electrónicos largos adecuadamente"""
        correo_largo = "a" * 312 + "@example.com"
        usuario_largo = Usuario("Juan", "Pérez", correo_largo, "contraseña_correcta", "2024-03-07", "activo", "normal")
        self.assertEqual(usuario_largo.Iniciar_sesion(), "Error: Correo electrónico inválido")

    def test_inicio_sesion_correo_incorrecto(self):
        """Debe fallar el inicio de sesión con un correo incorrecto"""
        usuario_incorrecto = Usuario("Juan", "Pérez", "usuario@incorrecto.com", "contraseña_correcta", "2024-03-07", "activo", "normal")
        self.assertEqual(usuario_incorrecto.Iniciar_sesion(), "Error: Usuario no encontrado")

    def test_inicio_sesion_contraseña_incorrecta(self):
        """Debe fallar el inicio de sesión con una contraseña incorrecta"""
        usuario_mal_pass = Usuario("Juan", "Pérez", "usuario@example.com", "contraseña_incorrecta", "2024-03-07", "activo", "normal")
        self.assertEqual(usuario_mal_pass.Iniciar_sesion(), "Error: Contraseña incorrecta")

    def test_inicio_sesion_usuario_inactivo(self):
        """Debe fallar el inicio de sesión si el usuario está inactivo"""
        usuario_inactivo = Usuario("Ana", "Gómez", "usuario@example.com", "contraseña_correcta", "2024-03-07", "inactivo", "normal")
        self.assertEqual(usuario_inactivo.Iniciar_sesion(), "Error: Usuario inactivo")

if __name__ == "__main__":
    unittest.main()
