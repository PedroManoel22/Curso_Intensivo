# 8.10 – Grandes mágicos: Comece com uma cópia de seu programa do Exercício
# 8.9. Escreva uma função chamada make_great() que modifique a lista de
# mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame
# show_magicians() para ver se a lista foi realmente modificada.


def show_magicians(magicians: list[str]) -> str:
    if not magicians:
        return "Nenhum mágico na lista"

    names = "\n".join(magicians)

    return f"Nomes dos mágicos:\n{names}\n"


def make_great(magicians: list[str]) -> list[str]:

    magicians_great = [f"Grande {mag}" for mag in magicians]
    return magicians_great


if __name__ == "__main__":
    magicians = [
        "Houdini",
        "Fu-Manchu",
        "Richiardi Jr",
        "Jasper Maskelyne",
        "Dai Vernon",
        "David Blaine",
    ]

    list1 = show_magicians(magicians)
    print(list1)

    lis2 = make_great(magicians)
    print(show_magicians(lis2))
