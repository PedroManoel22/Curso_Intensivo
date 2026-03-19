# 10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
# 10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.

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
        pass
