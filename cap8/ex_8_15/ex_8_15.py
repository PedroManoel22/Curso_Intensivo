# 8.15 – Impressão de modelos: Coloque as funções do exemplo print_models.py
# em um arquivo separado de nome printing_functions.py. Escreva uma instrução
# import no início de print_models.py e modifique o arquivo para usar as funções
# importadas.

from printing_functions import print_models, show_completed_models

unprinted_designs = ["Keychain", "headphone cover", "cell phone support"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
