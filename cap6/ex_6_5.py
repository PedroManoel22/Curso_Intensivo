# 6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
# cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
# • Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
# pelo Egito. ✔️
# • Use um laço para exibir o nome de cada rio incluído no dicionário.
# • Use um laço para exibir o nome de cada país incluído no dicionário.

rios = {
    "Amazona": "Brazil",
    "Mississipi": "Estados Unidos",
    "Paraná": "Brazil",
}

print()

for k, v in rios.items():
    print(f"O {k} corre pelo {v}")

print()

print("Nomes de cada rio:\n")

for k in rios.keys():
    print(k)

print()

print("Nome do país que cada rio corre:\n")

for v in rios.values():
    print(v)

print()
