# 10.13 – Verificando se é o usuário correto: A última listagem de
# remember_me.py supõe que o usuário já forneceu seu nome ou que o programa
# está executando pela primeira vez. Devemos modificá-lo para o caso de o usuário
# atual não ser a pessoa que usou o programa pela última vez.
# Antes de exibir uma mensagem de boas-vindas de volta em greet_user(),
# pergunte ao usuário se seu nome está correto. Se não estiver, chame
# get_new_username() para obter o nome correto

import json

from rich import print


def get_strored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username() -> str:
    """Pede um novo nome de usuário."""
    username = input("What is your name? ")
    filename = "username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_strored_username()

    if username:
        correct_name(username)
        print("Wecolme back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


def correct_name(name: str):
    while True:
        resp = input(f"Is your name is correct '{name}'? [S/N]: ").upper().strip()

        if resp == "N":
            name = get_new_username()

        elif resp == "S":
            return name

        else:
            print("\n[red]Please provide a valid answer, yes or no.\n[/]")


if __name__ == "__main__":
    greet_user()
