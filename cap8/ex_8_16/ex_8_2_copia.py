# 8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
# um parâmetro title. A função deve exibir uma mensagem como Um dos meus
# livros favoritos é Alice no país das maravilhas. Chame a função e não
# se esqueça de incluir o título do livro como argumento na chamada da função.


def favorite_book(name):
    print(f"\nUm dos meus livro favoritos é {name.title()}\n")


if __name__ == "__main__":
    favorite_book("o mundo assombrado pelos demônios")
