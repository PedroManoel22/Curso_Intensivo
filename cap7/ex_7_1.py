# 7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual
# tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
# exemplo, “Deixe-me ver se consigo um Subaru para você.”
from rich import print

while True:
    car = str(input("\nQual tipo de carro você gostaria de alugar? "))

    if car and all(c.isalpha() for c in car):
        break

    print(
        "\n⚠️[red]  Por favor, digite um nome de carro válido (apenas letras).[/]"
    )

print(f"\nDeixe me ver se consigo um {car} para você!\n")
