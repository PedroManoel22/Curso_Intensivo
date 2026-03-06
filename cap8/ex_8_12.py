# 8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
# pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
# itens quantos forem fornecidos pela chamada da função e deve apresentar um
# resumo do sanduíche pedido. Chame a função três vezes usando um número
# diferente de argumentos a cada vez.
from rich import print


def sanduiche(ham=list[str], itens=int) -> str:

    igredientes = ", ".join(ham)
    return (
        f"\nO sanduiche tem {itens} igredientes, são eles:\n"
        f"[yellow]{igredientes}[/]\n"
    )


if __name__ == "__main__":
    igredientes = [
        "Alface",
        "2 carnes de 100g",
        "Tomate",
        "Molho especial da casa",
        "pepino",
    ]
    total_igredientes = len(igredientes)
    sanduiche1 = sanduiche(igredientes, total_igredientes)
    print(sanduiche1)
