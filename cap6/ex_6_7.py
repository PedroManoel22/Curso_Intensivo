# 6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
# (página 147). Crie dois novos dicionários que representem pessoas diferentes e
# armazene os três dicionários em uma lista chamada people. Percorra sua lista de
# pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
# sabe sobre cada pessoa


pessoa1 = {
    "first_name": "Pedro",
    "last_name": "Manoel",
    "age": "25",
    "city": "Brasilia",
}

pessoa2 = {
    "first_name": "Maria",
    "last_name": "Luiza",
    "age": "16",
    "city": "João Pessoa",
}


pessoa3 = {
    "first_name": "Davi",
    "last_name": "LUiz",
    "age": "12",
    "city": "Itaporanga",
}

pessoas = [pessoa1, pessoa2, pessoa3]

print()

for p in pessoas:
    for k, v in p.items():
        print(f"{k} -> {v}")

    print()
