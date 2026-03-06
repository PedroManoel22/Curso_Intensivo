# 8.14 – Carros: Escreva uma função que armazene informações sobre um carro em
# um dicionário. A função sempre deve receber o nome de um fabricante e um
# modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
# Chame a função com as informações necessárias e dois outros pares nome-valor,
# por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma
# chamada como esta:
# car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
# Mostre o dicionário devolvido para garantir que todas as informações foram
# armazenadas corretamente.


def make_car(name: str, model: str, **others: str) -> str:
    informations = dict()
    informations["name"] = name
    informations["model"] = model

    for k, v in others.items():
        informations[k] = v

    return informations


if __name__ == "__main__":
    car = make_car("subaru", "outback", color="blue", tow_package=True)
    car2 = make_car("Fiat", "Uno", color="white", tow_package=True)
    print()
    print(car)
    print()
    print(car2)
    print()
