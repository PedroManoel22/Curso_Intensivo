# 10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
# pessoas por que elas gostam de programação. Sempre que alguém fornecer um
# motivo, acrescente-o em um arquivo que armazene todas as respostas.

from rich import print

adress = "Curso_Intensivo/cap10/ex10_5/respostas.txt"
while True:
    respostas = ["S", "N"]
    resp = input("\nPorque você gosta de programação? ")
    cont = input("Deseja continuar? ").upper().strip()

    with open(adress, "a", encoding="utf-8") as file_object:
        file_object.write(f"{resp}\n")

    if cont == "N":
        break

    elif cont not in respostas:
        print("\n[red]Por favor coloque uma resposta válida![/]\n")
