# 6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
# que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
# cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
# age e city. Mostre cada informação armazenada em seu dicionário.

pessoa = {
    "first_name": "Pedro",
    "last_name": "Manoel",
    "age": "25",
    "city": "Brasilia",
}

print()

for k, v in pessoa.items():
    print(f"{k}: {v}")

print()
