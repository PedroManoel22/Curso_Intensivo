# 9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
# classe chamada IceCreamStand que herde da classe Restaurant escrita no
# Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
# classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
# atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
# um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
# chame esse método.

from ex_9_1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Strawberry', 'Lemon', 'Watermelon', 'Grape']
    
    def show_flavors(self):
        print('\n---- Flavors ----')
        for f in self.flavors:
            print(f)
        print()

x = IceCreamStand('Pedro´S Ice cream', 'ice-cream parlor')
x.describe_restaurant()
x.show_flavors()
