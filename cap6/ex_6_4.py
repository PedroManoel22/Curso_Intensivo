# 6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um
# laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
# instruções print por um laço que percorra as chaves e os valores do dicionário.
# Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
# Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
# significados novos deverão ser automaticamente incluídos na saída

# Como já resolvi o exercício 6.3 com um laço for, vou apenas resolver o restante da questão
# ("acrescente mais cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
#  essas palavras e significados novos deverão ser automaticamente incluídos na saída").

glosario = {
    "Print": "Imprime algo no terminal",
    "Input": "Recebe algo do usuário",
    "Variável": "Um endereço na memória que recebe um valor",
    "String": "Uma variável, do tipo texto",
    "Int": "Uma variável, número (ex: 5) do tipo inteiro ",
    "Float": "Uma variável, número (com ponto flutuante. ex: 1.5) do tipo float",
    "Loop": "Estrutura de repetição, ex: for, while",
    "Classe": "Modelo para criar objetos",
    "Função": "Bloco de código reutilizável",
    "Comentário": "Texto ignorado pelo interpretador, iniciado com #  ou '''",
}

print()

for k, v in glosario.items():
    print(f"{k} -> {v}")

print()
