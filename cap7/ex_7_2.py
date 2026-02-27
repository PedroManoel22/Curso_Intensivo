# 7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
# quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
# exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
# contrário, informe que sua mesa está pronta.
from rich import print


def valida_num_int(pergunta):
    while True:
        try:
            qtd_pessoas = int(input(pergunta))

        except (ValueError, KeyboardInterrupt):
            print(f"\n[red]Por favor coloque um número inteiro![/]")

        else:
            return qtd_pessoas


if __name__ == "__main__":
    pergunta = "\nQuantas pessoas estão no seu grupo para o jantar? "
    qtd_pessoas = valida_num_int(pergunta)

    if qtd_pessoas > 8:
        print(
            f"\n[red]Ainda não temos mesa para [yellow]{qtd_pessoas}[/], por favor espere por uma mesa![/]\n"
        )

    else:
        print(
            f"\n[green]Sua mesa para [yellow]{qtd_pessoas}[/] pessoas já está pronta![/]\n"
        )
