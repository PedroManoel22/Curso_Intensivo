# 8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
# tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A
# função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem
# estampada.
# Chame a função uma vez usando argumentos posicionais para criar uma
# camiseta. Chame a função uma segunda vez usando argumentos nomeados.

from rich import print


def make_shirt(tamanho: str, msg: str):
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
    mensagem1 = "Caixaça"
    make_shirt(tamanho1, mensagem1)

    tamanho2 = "p"
    mensagem2 = "Olá, mundo!"
    make_shirt(tamanho=tamanho2, msg=mensagem2)
