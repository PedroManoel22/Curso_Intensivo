# 6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
# 147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
# apresente o nome de cada pessoa, juntamente com seus números favoritos.

favorite_numbers = {
    "Pedro": [46, 22],
    "Ana": [35],
    "João": [18],
    "Fernando": [27, 10, 20],
    "Isabel": [36, 8],
}

print()

for k, v in favorite_numbers.items():
    print(f"O número favorito de {k} é ", end="")
    for num in v:
        print(f"{num} ", end="")
    print()

print()
