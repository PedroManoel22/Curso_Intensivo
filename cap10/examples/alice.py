# Link para baixar o texto do livro alice no pais das maravilhas: https://www.gutenberg.org/files/11/11-0.txt

from rich import print

file_adress = "Curso_Intensivo/cap10/examples/alice.txt"
name = "alice.py"
try:
    with open(file_adress, encoding="utf-8") as file_ocject:
        contents = file_ocject.read()
except FileNotFoundError:
    msg = "\n[red]Sorry, the file " + file_adress + " does not exist.[/]\n"
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("\nThe file " + name + " has about " + str(num_words) + " words.\n")
