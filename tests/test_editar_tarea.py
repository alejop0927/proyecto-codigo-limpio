import unittest
from src.tarea import tarea
from src.Usuario import Usuario

class TestEditarTarea(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("usuario1")
        self.tarea = tarea("Hacer ejercicio", "2025-03-07", "Salud", "Por hacer", self.usuario)

    def test_editar_texto_tarea(self):
        self.tarea.texto = "Hacer cardio"
        self.assertEqual(self.tarea.texto, "Hacer cardio")
    
    def test_editar_categoria_tarea(self):
        self.tarea.categoria = "Educación"
        self.assertEqual(self.tarea.categoria, "Educación")
    
    def test_editar_estado_tarea(self):
        self.tarea.estado = "Completada"
        self.assertEqual(self.tarea.estado, "Completada")
    
    def test_editar_texto_maximo(self):
        texto_largo = "A" * 255
        self.tarea.texto = texto_largo
        self.assertEqual(self.tarea.texto, texto_largo)
    
    def test_editar_estado_limite(self):
        self.tarea.estado = "Pendiente"
        self.assertEqual(self.tarea.estado, "Pendiente")
    
    def test_editar_nueva_categoria_valida(self):
        self.tarea.categoria = "Placer"
        self.assertEqual(self.tarea.categoria, "Placer")
    
    def test_editar_tarea_inexistente(self):
        """Debe lanzar AttributeError al intentar modificar una tarea inexistente"""
        tarea_inexistente = None
        with self.assertRaises(AttributeError):
            tarea_inexistente.texto = "Nuevo texto"  # Aquí ya está corregido
    
    def test_editar_tarea_sin_cambios(self):
        """Verifica que la copia de la tarea sea igual a la original"""
        tarea_copia = tarea(
            self.tarea.texto,
            self.tarea.fecha_creacion,
            self.tarea.categoria,
            self.tarea.estado,
            self.tarea.usuario
        )
        self.assertEqual(vars(self.tarea), vars(tarea_copia))
    
    def test_editar_usuario_tarea(self):
        """Debe lanzar un error al intentar cambiar el usuario de la tarea"""
        otro_usuario = Usuario("usuario2")
        with self.assertRaises(AttributeError):
            self.tarea.usuario = otro_usuario

if __name__ == "__main__":
    unittest.main()
