# 8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
# aceite o nome de uma cidade e seu país. A função deve devolver uma string
# formatada assim:
# "Santiago, Chile"
# Chame sua função com pelo menos três pares cidade-país e apresente o valor
# devolvido.


def city_country(city, country):
    print(f"{city}, {country}")


if __name__ == "__main__":
    print()
    city_country("João Pessoa", "Brazil")
    city_country("Nova York", "EUA")
    city_country("Itaporanga", "Brazil")
    print()
