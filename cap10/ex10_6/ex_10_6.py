# 10.6 – Adição: Um problema comum quando pedir entradas numéricas ocorre
# quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
# entrada para um int, você obterá um TypeError. Escreva um programa que peça
# dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso
# algum dos valores de entrada não seja um número e apresente uma mensagem de
# erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite
# um texto no lugar de um número.

from rich import print


def valida_num() -> str:
    while True:
        try:
            num1 = float(input("\nInsira um número: "))
            num2 = float(input("\nInsira um outro número número: "))
            break

        except (TypeError, ValueError):
            print("\n[red]Por favor insira um número![/]")

    return soma_valores(num1, num2)


def soma_valores(x: float, y: float) -> str:
    return f"\n{x} + {y} = {x + y}"


if __name__ == "__main__":
    print(valida_num())
