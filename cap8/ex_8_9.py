# 8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
# função chamada show_magicians() que exiba o nome de cada mágico da lista.


def show_magicians(magicians: list[str]) -> str:
    if not magicians:
        return "Nenhum mágico na lista"

    names = "\n".join(magicians)

    return f"Nomes dos mágicos:\n{names}\n"


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
