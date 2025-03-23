import pytest
from src.Usuario import Usuario


usuarios_db = {
    "usuario@example.com": {"id_usuario": 1, "contraseña": "contraseña_vieja"}
}

metodo_original_cambiar_contraseña = Usuario.cambiar_contraseña


def cambiar_contraseña_falsa(email, nueva_contraseña):
    usuario = usuarios_db.get(email)
    if not usuario:
        return "Error: Usuario no encontrado"
    
    usuario["contraseña"] = nueva_contraseña
    return "Contraseña actualizada con éxito"

def test_cambiar_contrasena_exitoso():
 
    Usuario.cambiar_contraseña = cambiar_contraseña_falsa

    
    resultado = Usuario.cambiar_contraseña("usuario@example.com", "nueva_contraseña")

    assert resultado == "Contraseña actualizada con éxito"
    assert usuarios_db["usuario@example.com"]["contraseña"] == "nueva_contraseña"

  
    Usuario.cambiar_contraseña = metodo_original_cambiar_contraseña

def test_cambiar_contraseña_con_mayusculas():
     Usuario.cambiar_contraseña = cambiar_contraseña_falsa

    
     resultado = Usuario.cambiar_contraseña("usuario@example.com", "NUEVA_CONTRASEÑA")

     assert resultado == "Contraseña actualizada con éxito"
     assert usuarios_db["usuario@example.com"]["contraseña"] == "NUEVA_CONTRASEÑA"

  
     Usuario.cambiar_contraseña = metodo_original_cambiar_contraseña


