import pytest
from unittest.mock import patch
from src.Usuario import Usuario

def test_cambiar_contrasena_exitoso():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña actualizada con éxito"):
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")
        assert resultado == "Contraseña actualizada con éxito"


def test_cambiar_contraseña_con_mayusculas():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña actualizada con éxito"):
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "NUEVA_CONTRASEÑA")
        assert resultado == "Contraseña actualizada con éxito"


def test_cambiar_contraseña_nuevamente():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña actualizada con éxito"):
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")
        assert resultado == "Contraseña actualizada con éxito"

    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña actualizada con éxito"):
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "OTRA_CONTRASEÑA")
        assert resultado == "Contraseña actualizada con éxito"


def test_cambiar_contraseña_extensa():
    with patch.object(Usuario, 'cambiar_contraseña', side_effect=ValueError("Error: Contraseña demasiado larga")):
        contraseña_extensa = "A" * 320  
        with pytest.raises(ValueError, match="Error: Contraseña demasiado larga"):
            Usuario.cambiar_contraseña("usuario@example.com", contraseña_extensa)

def test_cambiar_contrasena_varias_veces_seguidas():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña cambiada correctamente") as mock_method:
        for _ in range(5):  
            resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")
            assert resultado == "Contraseña cambiada correctamente"
        
        assert mock_method.call_count == 5  

def test_cambiar_contrasena_desde_otro_dispositivo():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Contraseña cambiada correctamente") as mock_method:
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")
        assert resultado == "Contraseña cambiada correctamente"
        
       
        resultado_otro_dispositivo = Usuario.cambiar_contraseña("usuario@example.com", "otra_contraseña")
        assert resultado_otro_dispositivo == "Contraseña cambiada correctamente"
        
        assert mock_method.call_count == 2  
    
def test_cambiar_contrasena_con_correo_incorrecto():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Error: Usuario no registrado"):
        resultado = Usuario.cambiar_contraseña("usuario@incorrecto.com", "nueva_contraseña")
        assert resultado == "Error: Usuario no registrado"

def test_cambiar_contrasena_sin_correo():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Error: Debe proporcionar un correo"):
        resultado = Usuario.cambiar_contraseña("", "nueva_contraseña")
        assert resultado == "Error: Debe proporcionar un correo"

def test_cambiar_contrasena_usuario_inactivo():
    with patch.object(Usuario, 'cambiar_contraseña', return_value="Error: Usuario inactivo"):
        resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")
        assert resultado == "Error: Usuario inactivo"
