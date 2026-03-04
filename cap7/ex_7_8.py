# 7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os
# nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
# finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
# mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
# de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
# sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
# mensagem que liste cada sanduíche preparado.

sandwich_orders = ["HAMBURGÃO", "humburguinho", "bancozito", "BACOOON"]
finished_sandwiches = []

print()
for san in sandwich_orders:
    print(f"Preparei seu hamburguer chamado {san}")
    finished_sandwiches.append(san)

sandwich_orders.clear()

print()
print(f"Sanduíches preparados: ")
for san in finished_sandwiches:
    print(san)
print()
