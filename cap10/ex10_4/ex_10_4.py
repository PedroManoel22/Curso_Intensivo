# 10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
# usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
# acrescente uma linha que registre a visita do usuário em um arquivo chamado
# guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
# arquivo.

import sys
from pathlib import Path

from rich import print

# 1. Encontra a pasta 'cap10' (que é a pasta pai da pasta atual)
pasta_cap10 = Path(__file__).parent.parent  # retorna o caminho completo
sys.path.append(str(pasta_cap10))

# 2. Agora o Python "enxerga" a pasta ex10_3 como um módulo
from ex10_3.ex_10_3 import valida_nome  # noqa: E402

#                                       |-> este comentário diz ao ruff para não reclamar das ordens das importações


def saudar(nome: str) -> str:

    return f"Olá {nome}, prazer em lhe conhecer"


if __name__ == "__main__":
    nomes: list[str] = []

    while True:
        nome = valida_nome()
        saudacao = saudar(nome)

        resp = input("deseja continuar? [S/N]: ").upper()

        nomes.append(nome)

        if resp == "N":
            break

        elif resp == "S":
            continue

        else:
            print("\n[red]Por favor coloque uma resposta válida![/]\n")

    adress = "Curso_Intensivo/cap10/ex10_4/guest_book.txt"

    for nome in nomes:
        with open(adress, "a", encoding="utf-8") as file_object:
            file_object.write(f"{nome}\n")
