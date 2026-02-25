# 5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
# em uma cadeia if-elif-else.
# • Se o alienígena for verde, mostre uma mensagem informando que o jogador
# ganhou cinco pontos.
# • Se o alienígena for amarelo, mostre uma mensagem informando que o jogador
# ganhou dez pontos.
# • Se o alienígena for vermelho, mostre uma mensagem informando que o jogador
# ganhou quinze pontos.
# • Escreva três versões desse programa, garantindo que cada mensagem seja
# exibida para a cor apropriada do alienígena.

# executa o if
alien_color = "green"

if alien_color == "green":
    print(f"\nA cor do alienígena é verde!" "Parabéns você ganhou 5 pontos!\n")

elif alien_color == "yellow":
    print(
        f"\nA cor do alienígena é amarelo!" "Parabéns você ganhou 10 pontos!\n"
    )

else:
    print(
        f"\nA cor do alienígena é vermelhor!"
        "Parabéns você ganhou 15 pontos!\n"
    )

# executa o elif
alien_color = "yellow"

if alien_color == "green":
    print(f"\nA cor do alienígena é verde!" "Parabéns você ganhou 5 pontos!\n")

elif alien_color == "yellow":
    print(
        f"\nA cor do alienígena é amarelo!" "Parabéns você ganhou 10 pontos!\n"
    )

else:
    print(
        f"\nA cor do alienígena é vermelhor!"
        "Parabéns você ganhou 15 pontos!\n"
    )

# executa o else
alien_color = "red"

if alien_color == "green":
    print(f"\nA cor do alienígena é verde!" "Parabéns você ganhou 5 pontos!\n")

elif alien_color == "yellow":
    print(
        f"\nA cor do alienígena é amarelo!" "Parabéns você ganhou 10 pontos!\n"
    )

else:
    print(
        f"\nA cor do alienígena é vermelho!"
        "Parabéns você ganhou 15 pontos!\n"
    )
