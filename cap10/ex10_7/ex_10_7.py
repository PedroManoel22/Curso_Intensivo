# 10.7 – Calculadora para adição: Coloque o código do Exercício 10.6 em um
# laço while para que o usuário possa continuar fornecendo números, mesmo se
# cometerem um erro e digitarem um texto no lugar de um número.

# No exercício 10_6 já fiz isso, por tanto segue o código:


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
