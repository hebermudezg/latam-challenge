from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json
from memory_profiler import memory_usage

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Esta función toma la ruta de un archivo JSON que contiene tweets y devuelve una lista de las
    10 fechas con más tweets y el nombre del usuario que más publicó en cada una de esas fechas,
    optimizando para el uso de memoria.

    Parámetros:
    file_path (str): La ruta al archivo JSON que contiene los tweets.

    Retorna:
    List[Tuple[datetime.date, str]]: Una lista de tuplas donde cada tupla contiene una fecha (datetime.date)
    y el nombre del usuario que más publicó en esa fecha.
    """
    # Estructura para contar los tweets por fecha y por usuario
    date_counts = defaultdict(lambda: defaultdict(int))

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
            date = datetime.fromisoformat(tweet['date'][:10]).date()
            user = tweet['user']['username']
            date_counts[date][user] += 1 # Incrementar para la fecha y user correspondiente
        except (KeyError, ValueError) as e:
            print(f"[WARNING] Error procesando el tweet: {e}")

    # Obtener las 10 fechas con más tweets
    top_dates = sorted(date_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10] #x[1] conteos por usuario

    # Crear una lista de tuplas con las fechas y el nombre de usuario más activo en cada fecha
    result = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_dates] #sum(users.values())

    print(f"[INFO] Procesamiento completado exitosamente")
    return result