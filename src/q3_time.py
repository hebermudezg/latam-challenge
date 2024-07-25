from typing import List, Tuple
import re
from collections import defaultdict
import json

def extract_mentions(s: str) -> List[str]:
    return re.findall(r'@\w+', s)

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Esta función toma la ruta de un archivo JSON que contiene tweets y devuelve una lista de los
    10 usuarios más mencionados con su respectivo conteo, optimizando para el uso de memoria.

    Parámetros:
    file_path (str): La ruta al archivo JSON que contiene los tweets.

    Retorna:
    List[Tuple[str, int]]: Una lista de tuplas donde cada tupla contiene un usuario (str) y su conteo de menciones (int).
    """
    try:
        print(f"[INFO] Iniciando procesamiento del archivo: {file_path}")

        # Estructura para contar las menciones
        mention_counts = defaultdict(int)

        # Procesar el archivo línea por línea para minimizar el uso de memoria
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    tweet = json.loads(line)  # Convertir la línea en un diccionario de Python
                    content = tweet.get('content', '')  # Obtener el contenido del tweet, por defecto vacío si no existe
                    if content is not None:
                        # Extraer menciones del contenido del tweet
                        mentions_in_tweet = extract_mentions(content)
                        # Contar la frecuencia de cada mención
                        for mention in mentions_in_tweet:
                            mention_counts[mention] += 1
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    # Capturar y registrar cualquier error que ocurra durante el procesamiento del tweet
                    print(f"[WARNING] Error procesando el tweet: {e}")
                    continue

        # Obtener los 10 usuarios más mencionados
        top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        print(f"[INFO] Procesamiento completado exitosamente")
        return top_mentions

    except FileNotFoundError:
        # Manejar el caso en que el archivo no exista
        print(f"[ERROR] El archivo {file_path} no existe.")
        return []
