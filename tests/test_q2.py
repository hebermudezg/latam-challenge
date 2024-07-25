import unittest
from src.q2_time import q2_time
from src.q2_memory import q2_memory
from datetime import datetime
import tempfile
import json
import os
import emoji

class TestQ2(unittest.TestCase):
    
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

    def normalize_emojis(self, result):
        """
        Normaliza los emojis eliminando los modificadores de variación.
        """
        normalized_result = []
        for emoji_char, count in result:
            normalized_emoji = ''.join([c for c in emoji_char if c in emoji.EMOJI_DATA])
            normalized_result.append((normalized_emoji, count))
        return normalized_result

    def test_q2_time(self):
        # Llamar a la función con el archivo de prueba
        result = q2_time(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)

        # Normalizar los resultados
        normalized_result = self.normalize_emojis(result)
        
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
        
        # Normalizar el resultado esperado
        normalized_expected_result = self.normalize_emojis(expected_result)

        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(normalized_result), set(normalized_expected_result))

    def test_q2_memory(self):
        # Llamar a la función con el archivo de prueba
        result = q2_memory(self.test_file.name)
        
        # Imprimir el resultado para depuración
        print(result)

        # Normalizar los resultados
        normalized_result = self.normalize_emojis(result)
        
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

        # Normalizar el resultado esperado
        normalized_expected_result = self.normalize_emojis(expected_result)

        # Comparar los conjuntos en lugar de las listas
        self.assertEqual(set(normalized_result), set(normalized_expected_result))

if __name__ == '__main__':
    unittest.main()
