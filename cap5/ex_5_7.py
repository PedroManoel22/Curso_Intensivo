# 5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma
# série de instruções if independentes que verifiquem se determinadas frutas estão
# em sua lista.
# • Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
# • Escreva cinco instruções if. Cada instrução deve verificar se uma determinada
# fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por
# exemplo, Você realmente gosta de bananas!

favorite_fruits = ["banana", "melancia", "abacaxi"]

if "abacaxi" in favorite_fruits:
    print("\nVocê realmente gosta de abacaxi\n")

if "abacaxi" not in favorite_fruits:
    print("\nVocê realmente NÃO gosta de abacaxi\n")

if "mamão" in favorite_fruits:
    print("\nVocê realmente gosta de mamão!\n")

if "mamão" not in favorite_fruits:
    print("\nVocê realmente NÃO gosta de mamão!\n")

if "melancia" in favorite_fruits:
    print("\nVocê realmente gosta de melancia\n")

if "melancia" not in favorite_fruits:
    print("\nVocê realmente NÃO gosta de melancia\n")

if "melão" in favorite_fruits:
    print("\nVocê realmente gosta de melão!\n")

if "melão" not in favorite_fruits:
    print("\nVocê realmente NÃO gosta de melão!\n")
