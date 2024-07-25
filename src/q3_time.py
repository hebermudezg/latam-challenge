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
    # Estructura para contar las menciones
    mention_counts = defaultdict(int)

    # Procesar el archivo línea por línea para minimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet['content']
            mentions_in_tweet = extract_mentions(content)
            for mention in mentions_in_tweet:
                mention_counts[mention] += 1

    # Obtener los 10 usuarios más mencionados
    top_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return top_mentions