import unittest
from tarea import tarea
from Usuario import Usuario

class TestEditarTarea(unittest.TestCase):
    def setUp(self):
        """Configuración de usuario y tarea de prueba"""
        self.usuario = Usuario("Juan", "Pérez", "juan@example.com", "password123", "2024-03-07", "Activo", "Normal")
        self.tarea = tarea("Hacer ejercicio", "2025-03-07", "Salud", "Por hacer", self.usuario)

    def test_editar_texto_tarea(self):
        """Prueba editar el texto de la tarea"""
        self.tarea.texto = "Hacer cardio"
        self.assertEqual(self.tarea.texto, "Hacer cardio")
    
    def test_editar_categoria_tarea(self):
        """Prueba editar la categoría de la tarea"""
        self.tarea.categoria = "Educación"
        self.assertEqual(self.tarea.categoria, "Educación")
    
    def test_editar_estado_tarea(self):
        """Prueba editar el estado de la tarea"""
        self.tarea.estado = "Completada"
        self.assertEqual(self.tarea.estado, "Completada")
    
    def test_editar_texto_maximo(self):
        """Prueba editar el texto con un máximo de 255 caracteres"""
        texto_largo = "A" * 255
        self.tarea.texto = texto_largo
        self.assertEqual(self.tarea.texto, texto_largo)
    
    def test_editar_estado_limite(self):
        """Prueba cambiar el estado a un valor permitido"""
        self.tarea.estado = "Pendiente"
        self.assertEqual(self.tarea.estado, "Pendiente")
    
    def test_editar_nueva_categoria_valida(self):
        """Prueba cambiar la categoría a un nuevo valor válido"""
        self.tarea.categoria = "Placer"
        self.assertEqual(self.tarea.categoria, "Placer")
    
    def test_editar_tarea_inexistente(self):
        """Prueba modificar una tarea inexistente"""
        tarea_inexistente = None
        with self.assertRaises(AttributeError):
            tarea_inexistente.texto = "Nuevo texto"
    
    def test_editar_tarea_sin_cambios(self):
        """Prueba que una copia de la tarea sea igual a la original"""
        tarea_copia = tarea(self.tarea.texto, self.tarea.fecha_creacion, self.tarea.categoria, self.tarea.estado, self.tarea.usuario)
        self.assertEqual(vars(self.tarea), vars(tarea_copia))
    
    def test_editar_usuario_tarea(self):
        """Prueba cambiar el usuario de una tarea"""
        otro_usuario = Usuario("Pedro", "López", "pedro@example.com", "secure456", "2024-03-07", "Activo", "Normal")
        with self.assertRaises(AttributeError):
            self.tarea.usuario = otro_usuario

if __name__ == "__main__":
    unittest.main()
