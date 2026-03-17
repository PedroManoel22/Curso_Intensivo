from rich import print

adress = "Curso_Intensivo/cap10/pi_digits.txt"
adress2 = "Curso_Intensivo/cap9/oi.txt"
adress3 = r"c:\Users\Pedro\Documents\GitHub\Mundo_4\teste.txt"
adress4 = "Curso_Intensivo/cap10/pi_million_digits.txt"
# lendo o arquivo todo
print("\n[yellow]Lendo o arquivo todo:[/]")
with open(adress3, encoding="utf-8") as file_object:
    contents = file_object.read()
    print(contents)

# lendo linha por linha
print("[green]Lendo linha por linha:[/]\n")
with open(adress, encoding="utf-8") as file_object:
    for line in file_object:
        print(line)


# criando uma lista de linhas
print("\n[blue1]Criando uma lista de linhas:[/]\n")
with open(adress3, encoding="utf-8") as file_object:
    lines = file_object.readlines()

print(lines)


for line in lines:
    print(line.rstrip())

# criando uma única string contendo todos os dígitos do arquivo "pi_digits.txt"

print()

with open(adress) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(type(pi_string))
# toda vez que o Python ler um arquivo ele retorna uma string, se quisermos trabalhar com números deveremos convertê-lo para int() ou float()

# lendo os primeiro 52 digitos de pi

with open(adress4) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()
print("\nLendo os primeiros 52 digitos de pi:\n")
print(pi_string[:52] + "...")
print("\nQuantos caracteres tem o arquivo:\n")
print(len(pi_string))


# verificando se seu aniversário está nos primeiros 1 milão de digítos

birthday = input("\nInsira sua data de aniversário (sem /, apenas os números): ")

if birthday in pi_string:
    print("\n[green]Your birthday appears in the first million digits of pi![/]\n")

else:
    print(
        "\n[red]Your birthday does not appear in the first million digits of pi.[/]\n"
    )
