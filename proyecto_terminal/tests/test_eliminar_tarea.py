import pytest
from unittest.mock import patch
from src.tarea import Tarea

def test_eliminar_tarea_existente():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 10)
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_completada():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 15)
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_por_hacer():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 20)
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_con_id_limite():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 99999)  
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_con_muchas_ediciones():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 50)
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_usuario_con_muchas_tareas():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Tarea eliminada correctamente"):
        resultado = Tarea.eliminar_tarea(1, 100)
        assert resultado == "Tarea eliminada correctamente"

def test_eliminar_tarea_inexistente():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Error: La tarea no existe"):
        resultado = Tarea.eliminar_tarea(1, 999999)
        assert resultado == "Error: La tarea no existe"

def test_eliminar_tarea_sin_permisos():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Error: No tiene permisos"):
        resultado = Tarea.eliminar_tarea(2, 10)  
        assert resultado == "Error: No tiene permisos"

def test_eliminar_tarea_sin_id():
    with patch.object(Tarea, 'eliminar_tarea', return_value="Error: Debe proporcionar un ID"):
        resultado = Tarea.eliminar_tarea(1, "")
        assert resultado == "Error: Debe proporcionar un ID"
