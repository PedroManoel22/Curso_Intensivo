# 10.11 – Número favorito: Escreva um programa que pergunte qual é o número
# favorito de um usuário. Use json.dump() para armazenar esse número em um
# arquivo. Escreva um programa separado que leia esse valor e apresente a
# mensagem “Eu sei qual é o seu número favorito! É _____.”.
import json
from pathlib import Path

from rich import print


def validate_integer(num: str) -> bool:
    if num.isdigit():
        return True

    print("\n[red]Por favor coloque um número inteiro!\n[/]")
    return False


def get_number() -> int:
    while True:
        user_input = input("Qual é seu número favorito? ")
        if validate_integer(user_input):
            user_input_int = int(user_input)
            stores_number(user_input_int)
            return user_input_int


def stores_number(num: int):
    adress = Path(__file__).parent
    filename = "number.json"
    adress = adress / filename

    with open(adress, "w") as file_obj:
        json.dump(num, file_obj)


if __name__ == "__main__":
    get_number()
