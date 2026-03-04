# 8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
# camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
# uma camiseta grande e outra média com a mensagem default, e uma camiseta de
# qualquer tamanho com uma mensagem diferente.
from rich import print


def make_shirt(tamanho="gg", msg="Eu amo Python"):
    tamanhos = ["pp", "p", "m", "g", "gg"]
    tam = tamanho.lower()

    if tam in tamanhos:
        print(
            f"\nA camisa de tamanho: [yellow]{tam}[/] tem [green]{msg}[/] estampado nela!\n"
        )

    else:
        print("\n[red]Por favor insira um tamanho válido![/]\n")


if __name__ == "__main__":

    tamanho1 = "gg"
    make_shirt(tamanho1)

    tamanho2 = "m"
    make_shirt(tamanho=tamanho2)

    make_shirt(msg="Eu amo IA")
