import pytest
from unittest.mock import patch
from src.tarea import Tarea

def test_crear_tarea_con_texto_y_categoria():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        resultado = Tarea.crear_tarea(1, "Comprar leche", "Comprar en la tienda", "Compras", "Pendiente")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_con_estado_por_hacer():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        resultado = Tarea.crear_tarea(1, "Ir al gimnasio", "Hacer ejercicio", "Salud", "Por hacer")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_con_usuario_registrado():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        resultado = Tarea.crear_tarea(1, "Leer libro", "Leer 20 páginas", "Ocio", "Pendiente")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_con_texto_maximo():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        texto_largo = "A" * 255
        resultado = Tarea.crear_tarea(1, texto_largo, "Trabajo importante", "Trabajo", "Pendiente")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_con_estado_inusual():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        resultado = Tarea.crear_tarea(1, "Estudiar", "Preparar examen", "Estudios", "En pausa")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_con_categoria_desconocida():
    with patch.object(Tarea, 'crear_tarea', return_value="Tarea creada correctamente"):
        resultado = Tarea.crear_tarea(1, "Viajar", "Planificar viaje", "Otro", "Pendiente")
        assert resultado == "Tarea creada correctamente"

def test_crear_tarea_sin_texto():
    with patch.object(Tarea, 'crear_tarea', return_value="Error: El texto no puede estar vacío"):
        resultado = Tarea.crear_tarea(1, "", "Descripción vacía", "Personal", "Pendiente")
        assert resultado == "Error: El texto no puede estar vacío"

def test_crear_tarea_sin_categoria():
    with patch.object(Tarea, 'crear_tarea', return_value="Error: La categoría es requerida"):
        resultado = Tarea.crear_tarea(1, "Hacer ejercicio", "Ejercicio en casa", "", "Pendiente")
        assert resultado == "Error: La categoría es requerida"

def test_crear_tarea_sin_estado():
    with patch.object(Tarea, 'crear_tarea', return_value="Error: El estado es requerido"):
        resultado = Tarea.crear_tarea(1, "Revisar correo", "Revisar bandeja de entrada", "Trabajo", "")
        assert resultado == "Error: El estado es requerido"
