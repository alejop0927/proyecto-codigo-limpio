import unittest
from src.tarea import Tarea
from src.Usuario import Usuario

class TestEditarTarea(unittest.TestCase):
    def setUp(self):
        
        self.usuario = Usuario("Juan", "Pérez", "juan@example.com", "password123", "2024-03-07", "Activo", "Normal")
        self.Tarea = Tarea("Hacer ejercicio", "2025-03-07", "Salud", "Por hacer", self.usuario)

    def test_editar_texto_Tarea(self):
        
        self.Tarea.texto_tarea = "Hacer cardio"
        self.assertEqual(self.Tarea.texto, "Hacer cardio")
    
    def test_editar_categoria_Tarea(self):
       
        self.Tarea.categoria = "Educación"
        self.assertEqual(self.Tarea.categoria, "Educación")
    
    def test_editar_estado_Tarea(self):
        
        self.Tarea.estado = "Completada"
        self.assertEqual(self.Tarea.estado, "Completada")
    
    def test_editar_texto_maximo(self):
       
        texto_largo = "A" * 255
        self.Tarea.texto = texto_largo
        self.assertEqual(self.Tarea.texto, texto_largo)
    
    def test_editar_estado_limite(self):
        
        self.Tarea.estado = "Pendiente"
        self.assertEqual(self.Tarea.estado, "Pendiente")
    
    def test_editar_nueva_categoria_valida(self):
        
        self.Tarea.categoria = "Placer"
        self.assertEqual(self.Tarea.categoria, "Placer")
    
    def test_editar_Tarea_inexistente(self):
        
        Tarea_inexistente = None
        with self.assertRaises(AttributeError):
            Tarea_inexistente.texto = "Nuevo texto"
    
    def test_editar_Tarea_sin_cambios(self):
        
        Tarea_copia = Tarea(self.Tarea.texto, self.Tarea.fecha_creacion, self.Tarea.categoria, self.Tarea.estado, self.Tarea.usuario)
        self.assertEqual(vars(self.Tarea), vars(Tarea_copia))
    
    def test_editar_usuario_Tarea(self):
        
        otro_usuario = Usuario("Pedro", "López", "pedro@example.com", "secure456", "2024-03-07", "Activo", "Normal")
        with self.assertRaises(AttributeError):
            self.Tarea.usuario = otro_usuario

if __name__ == "__main__":
    unittest.main()
