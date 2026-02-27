# 6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
# dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
# tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
# chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
# isso, apresente tudo que você sabe sobre cada animal de estimação.

charles = {"nome_animal": "charles", "tipo": "dog", "nome_dono": "Isabel"}
jorginho = {
    "nome_animal": "jorginho",
    "tipo": "cockatiel",
    "nome_dono": "José",
}
oreo = {"nome_animal": "oreo", "tipo": "dog", "nome_dono": "Maria Luisa"}
cerafina = {"nome_animal": "cerafina", "tipo": "cat", "nome_dono": "Cecília"}

pets = [charles, jorginho, oreo, cerafina]

print()

for p in pets:
    for k, v in p.items():
        print(f"{k} -> {v}")
    print()
