# 4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
# laço for para exibir os números. (Se a saída estiver demorando demais, interrompa
# pressionando CTRL-C ou feche a janela de saída.)

numeros = [x for x in range(1, 1000001)]

for num in numeros:
    print(num)