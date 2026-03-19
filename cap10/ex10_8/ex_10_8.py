# 10.8 – Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo
# menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no
# segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o
# conteúdo do arquivo na tela. Coloque seu código em um bloco try-except para
# capturar o erro FileNotFound e apresente uma mensagem simpática caso o
# arquivo não esteja presente. Mova um dos arquivos para um local diferente de seu
# sistema e garanta que o código no bloco except seja executado de forma
# apropriada.

from pathlib import Path

from rich import print

absolute_path = Path(__file__).parent
filename_cats = "cats.txt"
filename_dogs = "dogs.txt"
cats = absolute_path / filename_cats
dogs = absolute_path / filename_dogs

files = [cats, dogs]

for file in files:
    try:
        with open(file) as f_object:
            content = f_object.read()

            print(f"\n[green]{Path(file).name}[/]\n\n{content}")

    except FileNotFoundError:
        print(f"[red]Sorry, the file [yellow]'{Path(file).name}'[/] does not exist![/]")
