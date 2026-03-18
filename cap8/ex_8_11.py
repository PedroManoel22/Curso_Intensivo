# 8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
# Chame a função make_great() com uma cópia da lista de nomes de mágicos.
# Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
# lista separada. Chame show_magicians() com cada lista para mostrar que você
# tem uma lista de nomes originais e uma lista com a expressão o Grande
# adicionada ao nome de cada mágico


def show_magicians(magicians_original: list[str], magicians_alterada: list[str]) -> str:
    if not magicians_original:
        return "Nenhum mágico na lista"

    names_original = "\n".join(magicians_original)
    names_alterada = "\n".join(magicians_alterada)

    return f"\nLista original:\n{names_original}\n\nLista alterada:\n{names_alterada}\n"


def make_great(magicians: list[str]) -> list[str]:
    magicians = magicians[:]

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

    lis2 = make_great(magicians)
    print(show_magicians(magicians, lis2))
