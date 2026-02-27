# 6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
# cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
# cada cidade e inclua o país em que a cidade está localizada, a população
# aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
# devem ser algo como country, population e fact. Apresente o nome de cada
# cidade e todas as informações que você armazenou sobre ela.

cities = {
    "São Paulo": {
        "country": "Brazil",
        "populacion": "11.9M",
        "fact": "São Paulo é o maior destino turístico do Brasil, com cerca de 14 milhões de turistas ao ano.",
    },
    "Brasília": {
        "country": "Brazil",
        "populacion": "3M",
        "fact": "Tempo de construção: 4 anos",
    },
    "João Pessoa": {
        "country": "Brazil",
        "populacion": "888.68K",
        "fact": "A primeira cidade a nascer o sol das Américas",
    },
}

print()
for k, v in cities.items():
    print(f"{k}: ", end="")

    for a, b in v.items():
        print(f"{a} -> {b} ", end="")

    print()
    print()

print()
