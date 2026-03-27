from pathlib import Path

from rich import print


def count_words(file_adress: str):
    """Conta o número aproximado de palavras em um arquivo"""

    # Pega o nome do arquivo
    filename = Path(file_adress).name
    try:
        with open(file_adress, encoding="utf-8") as file_ocject:
            contents = file_ocject.read()
    except FileNotFoundError:
        # msg = "\n[red]Sorry, the file " + filename + " does not exist.[/]\n"
        # print(msg)
        pass
    else:
        # Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)
        print("\nThe file " + filename + " has about " + str(num_words) + " words.\n")


if __name__ == "__main__":
    alice = "Curso_Intensivo/cap10/examples/alice.txt"
    siddhartha = "Curso_Intensivo/cap10/examples/siddhartha.txt"
    moby_dick = "Curso_Intensivo/cap10/examples/moby_dick.txt"
    little_woman = "Curso_Intensivo/cap10/examples/little_woman.txt"
    books = [alice, siddhartha, moby_dick, little_woman]

    for book in books:
        count_words(book)
