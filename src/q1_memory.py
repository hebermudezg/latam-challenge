from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import json

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
    def tweet_generator(file_path):
        """
        Generador que procesa el archivo línea por línea y convierte cada línea a un diccionario de Python.

        Parámetros:
        file_path (str): La ruta al archivo JSON que contiene los tweets.

        Yields:
        dict: Un diccionario representando un tweet.
        """
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
            # Extraer y validar la fecha del tweet
            date_str = tweet.get('date', None)
            if date_str:
                date = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
            else:
                continue  # Saltar si no hay fecha

            # Extraer y validar el usuario del tweet
            user = tweet['user']['username'] if tweet['user'] and 'username' in tweet['user'] else None
            if user:
                date_counts[date][user] += 1  # Incrementar el conteo para la fecha y usuario correspondiente

        except (KeyError, ValueError) as e:
            print(f"[WARNING] Error procesando el tweet: {e}")
            continue  # Saltar en caso de error de clave o valor

    # Obtener las 10 fechas con más tweets
    top_dates = sorted(date_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    # Crear una lista de tuplas con las fechas y el nombre de usuario más activo en cada fecha
    result = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_dates]

    print(f"[INFO] Procesamiento completado exitosamente")
    return result
