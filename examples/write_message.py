adress = "Curso_Intensivo/cap10/examples/"
name = "programming.txt"
adress = adress + name

# with open(adress, "w") as file_object:
#     # "r" -> modo de leitura, "w" -> modo de escrita, "a" -> modo de concatenação, "r+" -> ler e escrever
#     file_object.write("I love programming\n")
#     file_object.write("I love creating new games.\n")

# abrindo o arquivo no modo concatenação

with open(adress, "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
