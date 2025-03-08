import unittest
from src.Usuario import Usuario

class TestCambiarContraseña(unittest.TestCase):
    def setUp(self):
        """Configuración de usuarios de prueba"""
        self.usuario_activo = Usuario("usuario@example.com", "segura123")
        self.usuario_inactivo = Usuario("inactivo@example.com", "bloqueado", estado=False)

    def test_cambiar_contraseña_exitoso(self):
        resultado = self.usuario_activo.Cambiar_contraseña("usuario@example.com", "segura123", "nuevaClave456")
        self.assertEqual(resultado, "Contraseña cambiada correctamente")

    def test_cambiar_contraseña_mayusculas(self):
        resultado = self.usuario_activo.Cambiar_contraseña("USUARIO@EXAMPLE.COM".lower(), "segura123", "ClaveNueva123")
        self.assertEqual(resultado, "Contraseña cambiada correctamente")

    def test_cambiar_contraseña_despues_de_restablecer(self):
        self.usuario_activo.contraseña = "restaurada789"
        resultado = self.usuario_activo.Cambiar_contraseña("usuario@example.com", "restaurada789", "ClaveFinal123")
        self.assertEqual(resultado, "Contraseña cambiada correctamente")

    def test_cambiar_contraseña_muy_larga(self):
        nueva_clave = "a" * 321  
        resultado = self.usuario_activo.Cambiar_contraseña("usuario@example.com", "segura123", nueva_clave)
        self.assertEqual(resultado, "Error: Contraseña demasiado larga")

    def test_cambiar_contraseña_varios_intentos(self):
        for _ in range(3):  
            resultado = self.usuario_activo.Cambiar_contraseña("usuario@example.com", "segura123", "ClaveNueva123")
            self.assertEqual(resultado, "Contraseña cambiada correctamente")

    def test_cambiar_contraseña_otro_dispositivo(self):
        resultado = self.usuario_activo.Cambiar_contraseña("usuario@example.com", "segura123", "NuevaClaveDispositivo")
        self.assertEqual(resultado, "Contraseña cambiada correctamente")

    def test_cambiar_contraseña_correo_incorrecto(self):
        resultado = self.usuario_activo.Cambiar_contraseña("usuario@incorrecto.com", "segura123", "ClaveErronea")
        self.assertEqual(resultado, "Error: Usuario no registrado")

    def test_cambiar_contraseña_sin_correo(self):
        resultado = self.usuario_activo.Cambiar_contraseña("", "segura123", "ClaveNueva")
        self.assertEqual(resultado, "Error: Debe proporcionar un correo")

    def test_cambiar_contraseña_usuario_inactivo(self):
        resultado = self.usuario_inactivo.Cambiar_contraseña("inactivo@example.com", "bloqueado", "NuevaClaveInactivo")
        self.assertEqual(resultado, "Error: Usuario inactivo")

if __name__ == "__main__":
    unittest.main()
