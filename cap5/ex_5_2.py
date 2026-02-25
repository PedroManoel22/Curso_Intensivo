# 5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
# criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescente
# os em conditional_tests.py. Tenha pelo menos um resultado True e um False para
# cada um dos casos a seguir:
# • testes de igualdade e de não igualdade com strings;

print("testes de igualdade e de não igualdade com strings;")
cor = "Blue"
print("\nColor == Blue?", cor == cor)
print("\nColor == Black?", cor == "Black")

# • testes usando a função lower();

print("testes usando a função lower();")
string = "OI"
print("\nString == oi?", string == "oi")
print("\nColor == OI?", string == string.lower())
print()

# • testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
# maior ou igual a e menor ou igual a;

print(
    "testes numéricos que envolvam igualdade e não igualdade, maior e menor que,maior ou igual a e menor ou igual a;"
)
x = 1
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print()

# • testes usando as palavras reservadas and e or;

print("testes usando as palavras reservadas and e or;")
x = 1
y = 3
print(x == 1 and y == 2)
print()

# • testes para verificar se um item está em uma lista;

print("testes para verificar se um item está em uma lista;")
lista = [1, 2, 3]
n1 = 1
if n1 in lista:
    print(f"{n1} está na lista")

print()

# • testes para verificar se um item não está em uma lista.

print("testes para verificar se um item não está em uma lista.")
n2 = 5
if n2 not in lista:
    print(f"{n2} NÃO está na lista")
print()
