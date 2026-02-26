# 6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário
# de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
# • Pense em cinco palavras relacionadas à programação que você conheceu nos
# capítulos anteriores. Use essas palavras como chaves em seu glossário e
# armazene seus significados como valores.
# • Mostre cada palavra e seu significado em uma saída formatada de modo
# elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
# significado, ou apresentar a palavra em uma linha e então exibir seu significado
# indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n)
# para inserir uma linha em branco entre cada par palavra-significado em sua
# saída

glosario = {
    "Print": "Imprime algo no terminal",
    "Input": "Recebe algo do usuário",
    "Variável": "Um endereço na memória que recebe um valor",
    "String": "Uma variável, do tipo texto",
    "Int": "Uma variável, do tipo inteiro ",
}

print()

for k, v in glosario.items():
    print(f"{k} -> {v}")

print()
