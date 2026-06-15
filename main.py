import sys

from src.cargar_archivo import cargar_archivo
from src.solucion import hitting_set

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python3 {sys.argv[0]} <archivo>")
    else:
        jugadores = cargar_archivo(sys.argv[1])
        solucion = hitting_set(jugadores)
        print(f"Cantidad mínima: {len(solucion)} {solucion}")