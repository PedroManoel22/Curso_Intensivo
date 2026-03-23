# 10.12 – Lembrando o número favorito: Combine os dois programas do Exercício
# 10.11 em um único arquivo. Se o número já estiver armazenado, informe o número
# favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu número
# favorito e armazene-o em um arquivo. Execute o programa duas vezes para
# garantir que ele funciona.

import json
from pathlib import Path

adress = Path(__file__).parent
file_name = "favorite_number.json"
ADDRESS = adress / file_name


def validate_integer(num: str) -> bool:
    if num.isdigit():
        return True

    print("\n[red]Por favor coloque um número inteiro!\n[/]")
    return False


def number_exists():
    try:
        with open(ADDRESS, "r") as file_obj:
            favorite_number = json.load(file_obj)

    except FileNotFoundError:
        return get_number()
    else:
        return favorite_number


def write_number(num: int):
    with open(ADDRESS, "w") as file_obj:
        json.dump(num, file_obj)


def get_number() -> int:
    while True:
        user_input = input("Qual é seu número favorito? ")
        if validate_integer(user_input):
            user_input_int = int(user_input)
            write_number(user_input_int)
            return user_input_int


def show_number(num: int):
    print(f"Eu sei qual é o seu número favorito! É {num}.")


if __name__ == "__main__":
    favorite = number_exists()
    show_number(favorite)
