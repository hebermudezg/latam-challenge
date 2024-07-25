import unittest
from datetime import datetime
import tempfile
import json
import os
from src.q1_time import q1_time
from src.q1_memory import q1_memory

class TestQ1(unittest.TestCase):

    def setUp(self):
        # JSON temporal con algunos datos de prueba
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
            {"date": "2023-07-22T20:34:56Z", "user": {"username": "user4"}},
            {"date": "2023-07-23T20:34:56Z", "user": {"username": "user5"}},
            {"date": "2023-07-26T20:34:56Z", "user": {"username": "user6"}},
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
        # Definir el resultado esperado
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3'),
            (datetime(2023, 7, 22).date(), 'user2'),
            (datetime(2023, 7, 20).date(), 'user1'),
            (datetime(2023, 7, 23).date(), 'user5'),
            (datetime(2023, 7, 26).date(), 'user6')
        ]
        # Comparar los conjuntos (problema comparando lista por el orden)
        self.assertEqual(set(result), set(expected_result))

    def test_q1_memory(self):
        # Llamar a la función con el archivo de prueba
        result = q1_memory(self.test_file.name)
        # Definir el resultado esperado
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3'),
            (datetime(2023, 7, 22).date(), 'user2'),
            (datetime(2023, 7, 20).date(), 'user1'),
            (datetime(2023, 7, 23).date(), 'user5'),
            (datetime(2023, 7, 26).date(), 'user6')
        ]
        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(result), set(expected_result))

    def test_missing_date(self):
        # Crear un archivo JSON temporal con un tweet que no tiene fecha
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            tweets = [
                {"date": None, "user": {"username": "user1"}},
                {"date": "2023-07-21T16:34:56Z", "user": {"username": "user3"}},
            ]
            for tweet in tweets:
                temp_file.write(json.dumps(tweet) + '\n')
        # Llamar a las funciones con el archivo de prueba
        result_time = q1_time(temp_file.name)
        result_memory = q1_memory(temp_file.name)
        # Definir el resultado esperado
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3')
        ]
        # Comparar los resultados
        self.assertEqual(result_time, expected_result)
        self.assertEqual(result_memory, expected_result)
        os.remove(temp_file.name)

    def test_missing_user(self):
        # Crear un archivo JSON temporal con un tweet que no tiene usuario
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            tweets = [
                {"date": "2023-07-20T12:34:56Z", "user": None},
                {"date": "2023-07-21T16:34:56Z", "user": {"username": "user3"}},
            ]
            for tweet in tweets:
                temp_file.write(json.dumps(tweet) + '\n')
        # Llamar a las funciones con el archivo de prueba
        result_time = q1_time(temp_file.name)
        result_memory = q1_memory(temp_file.name)
        # Definir el resultado esperado
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3')
        ]
        # Comparar los resultados
        self.assertEqual(result_time, expected_result)
        self.assertEqual(result_memory, expected_result)
        os.remove(temp_file.name)

    def test_incorrect_date_format(self):
        # Crear un archivo JSON temporal con un tweet que tiene una fecha en formato incorrecto
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            tweets = [
                {"date": "2023/07/20", "user": {"username": "user1"}},
                {"date": "2023-07-21T16:34:56Z", "user": {"username": "user3"}},
            ]
            for tweet in tweets:
                temp_file.write(json.dumps(tweet) + '\n')
        # Llamar a las funciones con el archivo de prueba
        result_time = q1_time(temp_file.name)
        result_memory = q1_memory(temp_file.name)
        # Definir el resultado esperado
        expected_result = [
            (datetime(2023, 7, 21).date(), 'user3')
        ]
        # Comparar los resultados
        self.assertEqual(result_time, expected_result)
        self.assertEqual(result_memory, expected_result)
        os.remove(temp_file.name)

if __name__ == '__main__':
    unittest.main()
