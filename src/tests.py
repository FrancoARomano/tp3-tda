from src.solucion import hitting_set

# (subconjuntos, tamanio optimo esperado)
DATASETS = [
    (
        [
            ["Barcon't", "Cuti Romero", "Colidio", "Casco"],
            ["Colo Barco", "Wachoffisde Abila", "Messi", "Casco", "Armani", "Chiquito Romero"],
            ["Barcon't", "Wachoffisde Abila", "Colidio", "Casco"],
            ["Messi", "Cuti Romero", "Casco", "Pezzella"],
            ["Colo Barco", "Messi", "Cuti Romero"],
        ],
        2,
    ),
    (
        [
            ["Messi", "Di María"],
            ["Messi", "De Paul"],
            ["Messi", "Otamendi"],
        ],
        1,
    ),
    (
        [
            ["Messi"],
            ["Di María"],
            ["De Paul"],
            ["Otamendi"],
        ],
        4,
    ),
    (
        [
            ["A", "B", "C"],
            ["B", "D", "E"],
            ["C", "E", "F"],
            ["A", "D", "F"],
        ],
        2,
    ),
    (
        [
            ["Messi", "Lautaro", "Mac Allister"],
        ],
        1,
    ),
    (
        [
            ["Messi", "Lautaro", "De Paul", "Mac Allister"],
            ["Messi", "Lautaro"],
            ["Messi"],
        ],
        1,
    ),
]


def es_valida(subconjuntos, solucion):
    sol_set = set(solucion)
    return all(sol_set.intersection(s) for s in subconjuntos)


def correr_tests():
    todos_ok = True

    for i, (subconjuntos, optimo_esperado) in enumerate(DATASETS):
        sol = hitting_set(subconjuntos)
        valida = es_valida(subconjuntos, sol)
        optima = len(sol) == optimo_esperado

        if valida and optima:
            print(f"Test {i+1}: ✓  {sol}")
        else:
            print(f"Test {i+1}: ✗  {sol}  (esperado tamaño {optimo_esperado}, válida={valida})")
            todos_ok = False

    print()
    print("Todos los tests pasaron" if todos_ok else "Algunos tests fallaron")

if __name__ == "__main__":
    correr_tests()
