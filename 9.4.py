# 9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página 225). Acrescente um atributo chamado
# number_served cujo valor default é 0. Crie uma instância chamada restaurant a partir dessa classe. Apresente o
# número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o novamente.
# Adicione um método chamado set_number_served() que permita definir o número de clientes atendidos. Chame
# esse método com um novo número e mostre o valor novamente. ✔️
# Acrescente um método chamado increment_number_served() que permita incrementar o número de clientes
# servidos. Chame esse método com qualquer número que você quiser e que represente quantos clientes foram atendidos,
# por exemplo, em um dia de funcionamento.

class Restaurant:
    number_total = 0

    def __init__(self, restaurant_name, cuisine_type, number_served=0, open=False):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self._number_served = number_served  
        self.open = open
        self.number_total += number_served
            
    
         
    @property
    def number_served(self):
        return self._number_served
            
    @number_served.setter
    def number_served(self, new):
        self._number_served = new
            

    def describe_restaurant(self):
        print(f'\nName: {self.restaurant_name}\n'
              f'type: {self.cuisine_type}')


    def open_restaurant(self):
        print(f'\n\033[1;32mThe restaurant {self.restaurant_name} is open!\033[m')
        self.open = True

    
    def set_number_served(self, new_number):
        if self.open:
           self._number_served = new_number
           print(f'Updated list of served clients: {self._number_served}')

        else:
            print('\n\033[1;31mThe retaurant is closed!\033[m\n')
            print('It cannot serve any more customers\n')
    

    def increment_number_served(self):
        self.number_total += self.number_served
        print(f'\n{self.number_total} customers served today!')

        
restaurant = Restaurant('Pedro`s bar', 'Comida nordestina', 15)
restaurant.open_restaurant()
print(restaurant._number_served)
restaurant.set_number_served(2)
print(restaurant._number_served)
restaurant.increment_number_served()
