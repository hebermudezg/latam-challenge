import unittest
from src.q2_time import q2_time
from datetime import datetime
import tempfile
import json
import os

class TestQ2Time(unittest.TestCase):
    
    def setUp(self):
        # Crear un archivo JSON temporal con algunos datos de prueba
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
        tweets = [
            {"content": "Hello world 😊"},
            {"content": "Hello again 😂"},
            {"content": "I love coding ❤️"},
            {"content": "Python is awesome 🚀"},
            {"content": "Data science is fun 📊"},
            {"content": "I love emojis 😊"},
            {"content": "Emojis are cool 😎"},
            {"content": "Testing is important 🧪"},
            {"content": "Hello world 😊"}
        ]
        for tweet in tweets:
            self.test_file.write(json.dumps(tweet) + '\n')
        self.test_file.close()

    def tearDown(self):
        # Eliminar el archivo temporal después de la prueba
        os.remove(self.test_file.name)

    def test_q2_time(self):
        # Llamar a la función con el archivo de prueba
        result = q2_time(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            ('😊', 3), 
            ('😂', 1), 
            ('❤️', 1), 
            ('🚀', 1), 
            ('📊', 1), 
            ('😎', 1), 
            ('🧪', 1)
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

if __name__ == '__main__':
    unittest.main()
