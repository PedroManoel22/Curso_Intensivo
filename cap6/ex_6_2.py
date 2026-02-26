# 6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
# de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
# dicionário. Pense em um número favorito para cada pessoa e armazene cada um
# como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
# favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
# e obtenha alguns dados reais para o seu programa.

favorite_numbers = {
    "Pedro": 46,
    "Ana": 35,
    "João": 18,
    "Fernando": 27,
    "Isabel": 36,
}

print()

for k, v in favorite_numbers.items():
    print(f"O número favorito de {k} é {v}")

print()
