# 10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
# Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
from rich import print


def valida_nome() -> str:
    while True:
        nome = input("Insira seu nome: ")

        tem_numero = any(char.isdigit() for char in nome)

        if len(nome) <= 2 or tem_numero:
            print("\n\033[1;31mPor favor insira um nome válido!\033[m\n")
            continue

        else:
            return nome


if __name__ == "__main__":
    adress = "Curso_Intensivo/cap10/ex10_3/"
    file_name = "guest.txt"
    adress = adress + file_name
    name = valida_nome()
    with open(adress, "w") as file_object:
        file_object.write(f"{name}\n")

    print(f"[green]Nome: [yellow]'{name}'[/] salvo com sucesso em {adress}[/]")
