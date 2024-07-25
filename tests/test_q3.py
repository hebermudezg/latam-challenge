import unittest
from src.q3_time import q3_time
from src.q3_memory import q3_memory
import tempfile
import json
import os

class TestQ3(unittest.TestCase):
    
    def setUp(self):
        # JSON temporal con algunos datos de prueba
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
            {"content": "Hello world @user1"},
            {"content": None}
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

    def test_missing_content(self):
        # Crear un archivo JSON temporal con un tweet que tiene contenido faltante
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            tweets = [
                {"content": "Hello @user1"},
                {"content": None},
                {"content": "Data science is fun @user2"}
            ]
            for tweet in tweets:
                temp_file.write(json.dumps(tweet) + '\n')
        
        # Llamar a la función con el archivo de prueba
        result_time = q3_time(temp_file.name)
        result_memory = q3_memory(temp_file.name)
        
        # Imprimir los resultados para depuración
        print(result_time)
        print(result_memory)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            ('@user1', 1),
            ('@user2', 1)
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result_time), set(expected_result))
        self.assertEqual(set(result_memory), set(expected_result))

if __name__ == '__main__':
    unittest.main()
