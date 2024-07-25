from typing import List, Tuple
from collections import defaultdict
import json
import emoji

def extract_emojis_from_text(text: str) -> List[str]:
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
    try:
        print(f"[INFO] Iniciando procesamiento del archivo: {file_path}")

        # Estructura para contar los emojis
        emoji_counts = defaultdict(int)

        # Procesar el archivo línea por línea para minimizar el uso de memoria
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)  # Convertir la línea en un diccionario de Python
                    content = tweet.get('content', '')  # Obtener el contenido del tweet, por defecto vacío si no existe
                    if content is not None:
                        # Extraer emojis del contenido del tweet
                        emojis_in_tweet = extract_emojis_from_text(content)
                        # Contar la frecuencia de cada emoji
                        for em in emojis_in_tweet:
                            emoji_counts[em] += 1
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    # Captura y registra cualquier error que ocurra durante el procesamiento del tweet
                    print(f"[WARNING] Error procesando el tweet: {e}")
                    continue

        # Obtener los 10 emojis más usados
        top_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        print(f"[INFO] Procesamiento completado exitosamente")
        return top_emojis

    except FileNotFoundError:
        # Manejar el caso en que el archivo no exista
        print(f"[ERROR] El archivo {file_path} no existe.")
        return []