# 10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
# escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
# agora. Comece cada linha com a expressão Em Python podemos.... Salve o
# arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios
# deste capítulo. Escreva um programa que leia o arquivo e mostre o que você
# escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez
# percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma
# lista e então trabalhando com ela fora do bloco with.

adress = "Curso_Intensivo/cap10/ex10_1.py/learning_python.txt"

# lendo o arquivo todo

"""print()
with open(adress, encoding="utf-8") as file_object:
    file = file_object.read()
    print(file)

print()
"""
# percorrendo o objeto arquivo com um laço

"""print()
with open(adress, encoding="utf-8") as file_object:
    for line in file_object:
        print(line)
print()"""

# armazenando as linhas em uma lista e então trabalhando com ela fora do bloco with

with open(adress, encoding="utf-8") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
