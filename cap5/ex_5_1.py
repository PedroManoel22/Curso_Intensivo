# 5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
# frase que descreva o teste e o resultado previsto para cada um. Seu código deverá
# ser semelhante a:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Observe atentamente seus resultados e certifique-se de que compreende por que
# cada linha é avaliada como True ou False.
# • Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e
# outros cinco avaliados como False.

car: str = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")  # type: ignore

# 1
color: str = "blue"
print("\nIs color == 'blue'? I predict True.")
print(color == "blue")
print("\nIs color == 'black'? I predict False.")
print(color == "black")  # type: ignore

# 2
book: str = "A little prince"
print("\nIs book == 'A little prince'? I predict True.")
print(book == "A little prince")
print("\nIs book == 'IT'? I predict False.")
print(color == "IT")  # type: ignore

# 3
color: str = "black"
print("\nIs color == 'black'? I predict True.")
print(color == "black")
print("\nIs color == 'green'? I predict False.")
print(color == "green")  # type: ignore

# 4
price: str = "18"
print("\nIs price == '18'? I predict True.")
print(price == "18")
print("\nIs price == '20'? I predict False.")
print(price == "20")  # type: ignore

# 5
price: str = "20"
print("\nIs price == '20'? I predict True.")
print(price == "20")
print("\nIs price == '25'? I predict False.")
print(price == "25")  # type: ignore

# 6
car: str = "fiat"
print("\nIs car == 'fiat'? I predict True.")
print(car == "fiat")
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")  # type: ignore

# 7
color: str = "red"
print("\nIs color == 'red'? I predict True.")
print(color == "red")
print("\nIs color == 'white'? I predict False.")
print(color == "white")  # type: ignore

# 8
food: str = "pizza"
print("\nIs food == 'pizza'? I predict True.")
print(food == "pizza")
print("\nIs food == 'pasta'? I predict False.")
print(food == "pasta")  # type: ignore

# 9
clothing_brand: str = "nike"
print("\nIs clothing_brand == 'nike'? I predict True.")
print(clothing_brand == "nike")
print("\nIs clothing_brand == 'adidas'? I predict False.")
print(clothing_brand == "adidas")  # type: ignore

# 10
clothing_brand: str = "adidas"
print("\nIs clothing_brand == 'adidas'? I predict True.")
print(clothing_brand == "adidas")
print("\nIs clothing_brand == 'nike'? I predict False.")
print(clothing_brand == "nike")  # type: ignore
