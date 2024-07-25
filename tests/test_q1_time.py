import unittest
from src.q1_time import q1_time
from src.q1_memory import q1_memory
from datetime import datetime
import tempfile
import json
import os

class TestQ1Time(unittest.TestCase):
    
    def setUp(self):
        # Crear un archivo JSON temporal con algunos datos de prueba
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json')
        tweets = [
            {"date": "2023-07-20T12:34:56Z", "user": {"username": "user1"}},
            {"date": "2023-07-20T13:34:56Z", "user": {"username": "user2"}},
            {"date": "2023-07-20T14:34:56Z", "user": {"username": "user1"}},
            {"date": "2023-07-21T15:34:56Z", "user": {"username": "user3"}},
            {"date": "2023-07-21T16:34:56Z", "user": {"username": "user3"}},
            {"date": "2023-07-21T17:34:56Z", "user": {"username": "user3"}},
            {"date": "2023-07-22T18:34:56Z", "user": {"username": "user2"}},
            {"date": "2023-07-22T19:34:56Z", "user": {"username": "user2"}},
            {"date": "2023-07-22T20:34:56Z", "user": {"username": "user4"}}
        ]
        for tweet in tweets:
            self.test_file.write(json.dumps(tweet) + '\n')
        self.test_file.close()

    def tearDown(self):
        # Eliminar el archivo temporal después de la prueba
        os.remove(self.test_file.name)

    def test_q1_time(self):
        # Llamar a la función con el archivo de prueba
        result = q1_time(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3'),
            (datetime(2023, 7, 22).date(), 'user2'),
            (datetime(2023, 7, 20).date(), 'user1')
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

    def test_q1_memory(self):
        # Llamar a la función con el archivo de prueba
        result = q1_memory(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)
        
        # Verificar que la salida sea la esperada
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3'),
            (datetime(2023, 7, 22).date(), 'user2'),
            (datetime(2023, 7, 20).date(), 'user1')
        ]
        
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

if __name__ == '__main__':
    unittest.main()
