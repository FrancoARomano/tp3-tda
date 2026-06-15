def backtrack(actual, no_cubiertos, subconjuntos_set, mejor):
    if not no_cubiertos:
        if len(actual) < len(mejor["solucion"]):
            mejor["solucion"] = actual[:]
        return

    if len(actual) >= len(mejor["solucion"]):
        return

    pivot_idx = min(no_cubiertos, key=lambda i: len(subconjuntos_set[i]))

    for jugador in sorted(subconjuntos_set[pivot_idx]):
        nuevos_no_cubiertos = [i for i in no_cubiertos if jugador not in subconjuntos_set[i]]
        actual.append(jugador)
        backtrack(actual, nuevos_no_cubiertos, subconjuntos_set, mejor)
        actual.pop()


def hitting_set(subconjuntos):
    subconjuntos = [s for s in subconjuntos if s]
    if not subconjuntos:
        return []

    jugadores = sorted({j for s in subconjuntos for j in s})
    subconjuntos_set = [set(s) for s in subconjuntos]
    indices = list(range(len(subconjuntos_set)))

    mejor = {"solucion": list(jugadores)}
    backtrack([], indices, subconjuntos_set, mejor)
    return mejor["solucion"]