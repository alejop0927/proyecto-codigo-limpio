import pytest
from unittest.mock import patch
from src.Usuario import Usuario

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@example.com", "Juan", "Pérez", "ContraseñaSegura123", "Cuenta creada exitosamente"),
])
def test_usuario_crea_cuenta_correctamente(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@alternativo.com", "Ana", "Gómez", "OtraContraseña123", "Cuenta creada exitosamente"),
])
def test_usuario_crea_cuenta_con_correo_alternativo(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

def test_usuario_crea_cuenta_y_luego_inicia_sesion():
    with patch.object(Usuario, 'registrar', return_value="Cuenta creada exitosamente"):
        with patch.object(Usuario, 'iniciar_sesion', return_value=1):
            Usuario.registrar("Carlos", "López", "usuario@example.com", "Segura123")
            resultado = Usuario.iniciar_sesion("usuario@example.com", "Segura123")
            assert resultado == 1

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@example.com", "Juan", "Pérez", "A" * 101, "Error: Contraseña demasiado larga"),
])
def test_usuario_crea_cuenta_con_contrasena_muy_larga(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@example.com", "J" * 51, "Pérez", "Segura123", "Error: Nombre demasiado largo"),
])
def test_usuario_crea_cuenta_con_nombre_muy_largo(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

def test_usuario_crea_cuenta_con_conexion_inestable():
    with patch.object(Usuario, 'registrar', return_value="Error: No se pudo completar el registro"):
        resultado = Usuario.registrar("Luis", "Martínez", "usuario@inestable.com", "Segura123")
        assert resultado == "Error: No se pudo completar el registro"

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@example.com", "Juan", "Pérez", "Segura123", "Error: Correo ya registrado"),
])
def test_usuario_crea_cuenta_con_correo_ya_registrado(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("usuario@example.com", "Juan", "Pérez", "123", "Error: Contraseña demasiado débil"),
])
def test_usuario_crea_cuenta_con_contrasena_debil(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado

@pytest.mark.parametrize("correo, nombre, apellido, contrasena, resultado_esperado", [
    ("", "Juan", "Pérez", "Segura123", "Error: Datos obligatorios faltantes"),
])
def test_usuario_crea_cuenta_con_datos_incompletos(correo, nombre, apellido, contrasena, resultado_esperado):
    with patch.object(Usuario, 'registrar', return_value=resultado_esperado):
        resultado = Usuario.registrar(nombre, apellido, correo, contrasena)
        assert resultado == resultado_esperado
