# 7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
# que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
# Acrescente um código próximo ao início de seu programa para exibir uma
# mensagem informando que a lanchonete está sem pastrami e, então, use um laço
# while para remover todas as ocorrências de 'pastrami'  e sandwich_orders.
# Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
from rich import print

sandwich_orders = [
    "HAMBURGÃO",
    "pastrami",
    "humburguinho",
    "pastrami",
    "bancozito",
    "BACOOON",
    "pastrami",
]

finished_sandwiches = []

print()
print(f"Sanduíches a sereem feitos: {sandwich_orders}\n")
print("[red]Os sanduíches de pastrami acabaram![/]\n")
for san in sandwich_orders:
    if san != "pastrami":
        print(f"Preparei seu hamburguer chamado {san}")
        finished_sandwiches.append(san)

sandwich_orders.clear()

print()
print(f"Sanduíches preparados: ")
for san in finished_sandwiches:
    print(san)
print()
