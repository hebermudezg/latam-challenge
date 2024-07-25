import unittest
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import tempfile
import json
import os

class TestQ3(unittest.TestCase):
    
    def setUp(self):
        # Crear un archivo JSON temporal con algunos datos de prueba
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
        tweets = [
            {"content": "Hello @user1"},
            {"content": "Hello @user2 @user1"},
            {"content": "I love coding @user3"},
            {"content": "Python is awesome @user3"},
            {"content": "Data science is fun @user2"},
            {"content": "I love emojis @user1 @user2"},
            {"content": "Emojis are cool @user3"},
            {"content": "Testing is important @user4"},
            {"content": "Hello world @user1"}
        ]
        for tweet in tweets:
            self.test_file.write(json.dumps(tweet) + '\n')
        self.test_file.close()

    def tearDown(self):
        # Eliminar el archivo temporal después de la prueba
        os.remove(self.test_file.name)

    def test_q3_time(self):
        # Llamar a la función con el archivo de prueba
        result = q3_time(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            ('@user1', 4), 
            ('@user2', 3), 
            ('@user3', 3), 
            ('@user4', 1)
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

    def test_q3_memory(self):
        # Llamar a la función con el archivo de prueba
        result = q3_memory(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            ('@user1', 4), 
            ('@user2', 3), 
            ('@user3', 3), 
            ('@user4', 1)
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

if __name__ == '__main__':
    unittest.main()
