import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from random import seed, randint, sample
import numpy as np
import scipy as sp
from matplotlib import pyplot as plt
import seaborn as sns

from src.solucion import hitting_set
from util import time_algorithm

seed(22579)
np.random.seed(22579)

sns.set_theme()


def generar_subconjuntos(n):
    cantidad_jugadores = [f"j{i}" for i in range(n)]
    cantidad = 2 * n
    tam_max = max(2, n // 2)
    return [[cantidad_jugadores[i] for i in sample(range(n), randint(2, tam_max))] for _ in range(cantidad)]

x = np.arange(2, 21).astype(int)
results = time_algorithm(hitting_set, x, lambda n: [generar_subconjuntos(n)])

tiempos = [results[n] for n in x]

f_teorica = lambda n, c1, c2: c1 * n * 2**n + c2

c_opt, _ = sp.optimize.curve_fit(f_teorica, x, tiempos, p0=[1e-9, 0], maxfev=10000)

fig, ax = plt.subplots()
ax.plot(x, tiempos, label="Medición")
ax.plot(x, [f_teorica(n, c_opt[0], c_opt[1]) for n in x], "r--", label=r"Ajuste $n \cdot 2^n$")
ax.set_title("Tiempo de ejecución de hitting_set")
ax.set_xlabel("Cantidad de jugadores")
ax.set_ylabel("Tiempo de ejecución (s)")
ax.legend()
plt.savefig("complejidad_hitting_set.png", dpi=150, bbox_inches="tight")
plt.show()

errores = [abs(f_teorica(n, c_opt[0], c_opt[1]) - results[n]) for n in x]
print(f"Error cuadrático total para n·2^n: {np.sum(np.power(errores, 2)):.6e}")

fig2, ax2 = plt.subplots()
ax2.plot(x, errores, label=r"Error ajuste $n \cdot 2^n$")
ax2.set_title("Error de ajuste")
ax2.set_xlabel("Cantidad de jugadores")
ax2.set_ylabel("Error absoluto (s)")
ax2.legend()
plt.savefig("error_ajuste_hitting_set.png", dpi=150, bbox_inches="tight")
plt.show()