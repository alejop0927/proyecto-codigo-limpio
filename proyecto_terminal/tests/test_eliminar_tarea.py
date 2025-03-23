import unittest
from src.tarea import tarea
from src.Usuario import Usuario

class TestEliminarTarea(unittest.TestCase):
    def setUp(self):
        self.usuario1 = Usuario("Juan", "Pérez", "juan@example.com", "12345", "2025-03-07", "activo", "normal")
        self.usuario2 = Usuario("Ana", "López", "ana@example.com", "67890", "2025-03-07", "activo", "normal")

        self.tarea1 = tarea("Comprar leche", "2025-03-07", "Compras", "Por hacer", self.usuario1)
        self.tarea2 = tarea("Leer libro", "2025-03-07", "Educación", "Completada", self.usuario1)
        self.tarea_inexistente = None  
    def test_eliminar_tarea_existente(self):
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_completada(self):
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_por_hacer(self):
        tarea_nueva = tarea("Hacer ejercicio", "2025-03-07", "Salud", "Por hacer", self.usuario1)
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_id_limite(self):
        tarea_nueva = tarea("Viajar", "2025-03-07", "Placer", "En pausa", self.usuario1)
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_muchas_ediciones(self):
        tarea_nueva = tarea("Proyecto", "2025-03-07", "Trabajo", "En progreso", self.usuario1)
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_usuario_muchas_tareas(self):
        for i in range(50):
            tarea(f"Tarea {i}", "2025-03-07", "General", "Por hacer", self.usuario1)
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Tarea eliminada correctamente")

    def test_eliminar_tarea_inexistente(self):
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Error: La tarea no existe")

    def test_eliminar_tarea_sin_permisos(self):
        resultado = self.usuario2.Eliminar_tarea()
        self.assertEqual(resultado, "Error: No tiene permisos")

    def test_eliminar_tarea_sin_id(self):
        resultado = self.usuario1.Eliminar_tarea()
        self.assertEqual(resultado, "Error: Debe proporcionar un ID")

if __name__ == '__main__':
    unittest.main()
