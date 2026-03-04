# 8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
# uma frase informando a todos o que você está aprendendo neste capítulo. Chame
# a função e certifique-se de que a mensagem seja exibida corretamente.


def display_message(msg):
    print(f"\n{msg}\n")


if __name__ == "__main__":
    mensagem = "Olá tudo bem ?"
    display_message(mensagem)
