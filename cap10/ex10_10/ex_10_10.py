# 10.10 – Palavras comuns: Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e
# encontre alguns textos que você gostaria de analisar. Faça download dos arquivos
# texto dessas obras ou copie o texto puro de seu navegador para um arquivo-texto
# em seu computador.
# Você pode usar o método count() para descobrir quantas vezes uma palavra ou
# expressão aparece em uma string. Por exemplo, o código a seguir conta quantas
# vezes a palavra 'row' aparece em uma string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Observe que converter a string para letras minúsculas usando lower() faz com
# que todas as formas da palavra que você está procurando sejam capturadas,
# independentemente do modo como elas estiverem grafadas.
# Escreva um programa que leia os arquivos que você encontrou no Projeto
# Gutenberg e determine quantas vezes a palavra 'the' aparece em cada texto.

from pathlib import Path

from rich import print

adress_absolute = Path(__file__).parent

filename_little_woman = "little_woman.txt"
filename_moby_dick = "moby_dick.txt"
filename_siddhartha = "siddhartha.txt"

little_woman = adress_absolute / filename_little_woman
moby_dick = adress_absolute / filename_moby_dick
siddhartha = adress_absolute / filename_siddhartha

books = [little_woman, moby_dick, siddhartha]

for book in books:
    with open(book, "r", encoding="utf-8") as f_object:
        content = f_object.read()
        qtd_the = content.lower().count("the")
        print(f"\n[blue1]{Path(book).name}[/]\nAparece 'the' {qtd_the} vezes!")
