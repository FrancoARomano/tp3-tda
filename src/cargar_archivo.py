import csv
from os.path import exists

def cargar_archivo(nombre_archivo):
    if not exists(nombre_archivo):
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return None

    jugadores = []
    try:
        with open(nombre_archivo, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    jugadores_fila = [jugador.strip() for jugador in row if jugador.strip()]
                    if jugadores_fila:
                        jugadores.append(jugadores_fila)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

    return jugadores