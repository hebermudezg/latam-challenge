from typing import List, Tuple
from collections import defaultdict
import json
import emoji

def extract_emojis_from_text(text):
    return [c for c in text if c in emoji.EMOJI_DATA]

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Esta función toma la ruta de un archivo JSON que contiene tweets y devuelve una lista de los
    10 emojis más usados con su respectivo conteo, optimizando para el uso de memoria.

    Parámetros:
    file_path (str): La ruta al archivo JSON que contiene los tweets.

    Retorna:
    List[Tuple[str, int]]: Una lista de tuplas donde cada tupla contiene un emoji (str) y su conteo (int).
    """

    # Estructura para contar los emojis
    emoji_counts = defaultdict(int)

    # Función generadora para procesar el archivo línea por línea
    def tweet_generator(file_path): #iterador
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    yield json.loads(line)
        except FileNotFoundError:
            print(f"[ERROR] El archivo {file_path} no existe.")
            raise

    # Usar el generador para procesar cada tweet
    for tweet in tweet_generator(file_path):
        try:
            content = tweet['content']
            emojis_in_tweet = extract_emojis_from_text(content)
            for em in emojis_in_tweet:
                emoji_counts[em] += 1
        except KeyError as e:
            print(f"[WARNING] Error procesando el tweet: {e}")

    # Obtener los 10 emojis más usados
    top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    print(f"[INFO] Procesamiento completado exitosamente")
    return top_emojis
