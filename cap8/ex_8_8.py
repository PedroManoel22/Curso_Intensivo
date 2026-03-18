# 8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
# Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
# título de um álbum. Depois que tiver essas informações, chame make_album() com
# as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
# valor de saída no laço while

import re

from rich import print


def make_album(name: str, title: str, tracks: int = 0) -> dict[str, str]:
    album: dict[str, str] = dict()
    album["name"] = name
    album["title"] = title
    if tracks > 0:
        album["tracks"] = str(tracks)
    return album


def is_valid_name(name: str) -> bool:
    """
    Valida se uma string é um nome próprio real.

    Critérios:
    1. Não pode ser vazio.
    2. Deve conter apenas letras e espaços (incluindo acentos).
    3. Deve ter pelo menos um sobrenome (opcional, dependendo da regra de negócio).
    """
    if not name:
        return False

    # Limpa espaços extras no início, fim e entre palavras (strip + join/split)
    clean_name = " ".join(name.split())

    # Regex que aceita letras unicode (acentos) e espaços
    # ^[a-zA-ZÀ-ÿ ]+$ cobre a maioria dos caracteres latinos
    pattern = r"^[A-Za-zÀ-ÖØ-öø-ÿ\s']+$"

    if not re.match(pattern, clean_name):
        return False

    return len(clean_name.split()) >= 2


def is_valid_title(name: str) -> bool:
    """
    Valida se uma string é um nome real.

    Critérios:
    1. Não pode ser vazio.
    2. Deve conter apenas letras e espaços (incluindo acentos).
    """
    if not name:
        return False

    else:
        return True


if __name__ == "__main__":
    while True:
        name = str(input("\nInsira o nome e sobrenome do artista: "))
        title = str(input(f"\nInsira o nome do albúm do(a) contor(a) {name}: "))
        ret_name = is_valid_name(name)
        ret_title = is_valid_title(title)

        if not ret_name:
            print("\n[red]Por favor insira seu nome e sobrenome![/]")

        if not ret_title:
            print("\n[red]Por favor insira um nome do albúm válido![/]")

        elif ret_name and ret_title:
            print(f"\n{make_album(name, title)}\n")

            resp = str(input("Deseja sair (S/N)? ")).upper()

            if resp == "S":
                break

    print("\n[red]Obrigado e volte sempre! :+1:[/]")
