from typing import List, Tuple
import re
from collections import defaultdict
import json

def extract_mentions(s):
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
                    tweet = json.loads(line)
                    content = tweet['content']
                    mentions_in_tweet = extract_mentions(content)
                    for mention in mentions_in_tweet:
                        mention_counts[mention] += 1
                except (json.JSONDecodeError, KeyError, ValueError) as e:
                    print(f"[WARNING] Error procesando el tweet: {e}")
                    continue

        # Obtener los 10 usuarios más mencionados
        top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        print(f"[INFO] Procesamiento completado exitosamente")
        return top_mentions

    except FileNotFoundError:
        print(f"[ERROR] El archivo {file_path} no existe.")
        return []