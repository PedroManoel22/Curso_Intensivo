# 10.2 – Aprendendo C: Você pode usar o método replace() para substituir
# qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rápido
# que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Leia cada linha do arquivo learning_python.txt que você acabou de criar e
# substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre
# cada linha modificada na tela.

from pathlib import Path

from rich import print

path = Path(__file__).parent.parent / "ex10_1" / "learning_python.txt"

try:
    content = path.read_text(encoding="utf-8")
    content = content.replace("Python", "C")
    print(content)
except FileNotFoundError:
    print("[red]Erro: O arquivo não foi encontrado no caminho especificado.[/]")
