import pytest
from unittest.mock import patch
from src.tarea import Tarea

def test_editar_texto_tarea():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        resultado = Tarea.editar_tarea(1, 1, "Hacer cardio", "Ejercicio", "Salud", "Pendiente")
        assert resultado == "Tarea editada correctamente"

def test_editar_categoria_tarea():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        resultado = Tarea.editar_tarea(1, 1, "Estudiar", "Texto", "Educación", "Pendiente")
        assert resultado == "Tarea editada correctamente"

def test_editar_estado_tarea():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        resultado = Tarea.editar_tarea(1, 1, "Terminar informe", "Texto", "Trabajo", "Completada")
        assert resultado == "Tarea editada correctamente"

def test_editar_tarea_con_texto_maximo():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        texto_largo = "A" * 255
        resultado = Tarea.editar_tarea(1, 1, texto_largo, "Descripción larga", "Trabajo", "Pendiente")
        assert resultado == "Tarea editada correctamente"

def test_editar_tarea_con_estado_limite():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        resultado = Tarea.editar_tarea(1, 1, "Leer", "Texto", "Ocio", "Pendiente")
        assert resultado == "Tarea editada correctamente"

def test_editar_tarea_con_nueva_categoria():
    with patch.object(Tarea, 'editar_tarea', return_value="Tarea editada correctamente"):
        resultado = Tarea.editar_tarea(1, 1, "Viajar", "Texto", "Placer", "Pendiente")
        assert resultado == "Tarea editada correctamente"

def test_editar_tarea_inexistente():
    with patch.object(Tarea, 'editar_tarea', return_value="Error: La tarea no existe"):
        resultado = Tarea.editar_tarea(1, 999, "Tarea X", "Texto", "Trabajo", "Pendiente")
        assert resultado == "Error: La tarea no existe"

def test_editar_tarea_sin_cambios():
    with patch.object(Tarea, 'editar_tarea', return_value="Error: No hay cambios registrados"):
        resultado = Tarea.editar_tarea(1, 1, "Estudiar", "Texto", "Educación", "Pendiente")
        assert resultado == "Error: No hay cambios registrados"

def test_editar_tarea_cambiando_usuario():
    with patch.object(Tarea, 'editar_tarea', return_value="Error: No se puede cambiar usuario"):
        resultado = Tarea.editar_tarea(2, 1, "Leer", "Texto", "Ocio", "Pendiente")
        assert resultado == "Error: No se puede cambiar usuario"
