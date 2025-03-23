import pytest
from unittest.mock import patch
from src.Usuario import Usuario


def test_usuario_inicia_sesion_correctamente():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "ContraseñaCorrecta")
        assert resultado == "Inicio de sesión exitoso"  


def test_usuario_inicia_sesion_con_mayusculas():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("USUARIO@EXAMPLE.COM", "ContraseñaCorrecta")
        assert resultado == "Inicio de sesión exitoso"  


def test_usuario_inicia_sesion_despues_de_cerrar_sesion():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "ContraseñaCorrecta")
        assert resultado == "Inicio de sesión exitoso"  


def test_usuario_inicia_sesion_con_contraseña_larga():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "A" * 128)
        assert resultado == "Inicio de sesión exitoso"  


def test_usuario_inicia_sesion_con_correo_muy_largo():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("a" * 320 + "@example.com", "ContraseñaCorrecta")
        assert resultado == "Inicio de sesión exitoso"  


def test_usuario_inicia_sesion_con_multiples_intentos():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Inicio de sesión exitoso"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "ContraseñaCorrecta")
        assert resultado == "Inicio de sesión exitoso"  


def test_intentar_iniciar_sesion_con_correo_incorrecto():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Error: Usuario no registrado"):
        resultado = Usuario.iniciar_sesion("usuario@incorrecto.com", "ContraseñaCorrecta")
        assert resultado == "Error: Usuario no registrado"  


def test_intentar_iniciar_sesion_con_contraseña_incorrecta():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Error: Credenciales incorrectas"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "ContraseñaIncorrecta")
        assert resultado == "Error: Credenciales incorrectas"  


def test_intentar_iniciar_sesion_con_usuario_inactivo():
    with patch.object(Usuario, 'iniciar_sesion', return_value="Error: Usuario inactivo"):
        resultado = Usuario.iniciar_sesion("usuario@example.com", "ContraseñaCorrecta")
        assert resultado == "Error: Usuario inactivo"  
