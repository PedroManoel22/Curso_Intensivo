# 8.16 – Importações: Usando um programa que você tenha escrito e que contenha
# uma única função, armazene essa função em um arquivo separado. Importe a
# função para o arquivo principal de seu programa e chame-a usando cada uma das
# seguintes abordagens:
# import nome_do_módulo
# from nome_do_módulo import nome_da_função
# from nome_do_módulo import nome_da_função as nf
# import nome_do_módulo as nm
# from nome_do_módulo import *

import ex_8_2_copia  # 1
import ex_8_2_copia as nm  # 4
from ex_8_2_copia import *
from ex_8_2_copia import favorite_book  # 2
from ex_8_2_copia import favorite_book as nf  # 3

# 1
my_favorite_book = "IT"
ex_8_2_copia.favorite_book(my_favorite_book)

# 2
favorite_book(my_favorite_book)

# 3
nf(my_favorite_book)

# 4
nm.favorite_book(my_favorite_book)

# 5

ex_8_2_copia.favorite_book(my_favorite_book)
