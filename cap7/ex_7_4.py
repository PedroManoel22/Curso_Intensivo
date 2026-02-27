# 7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
# fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
# fornecido. À medida que cada ingrediente é especificado, apresente uma
# mensagem informando que você acrescentará esse ingrediente à pizza.
from rich import print

igrediente = ""
while igrediente != "quit":
    try:
        igrediente = str(
            input(
                "\nInsira um ingrediente para a pizza (digite quit, para finalizar): "
            )
        )

    except ValueError:
        print("\n[red]Por favor coloque um inrediente válido![/]")

    else:
        if igrediente != "quit":
            print(f"\n{igrediente} será adicionado na pizza!")
