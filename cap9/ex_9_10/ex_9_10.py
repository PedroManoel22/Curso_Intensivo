# 9.10 – Importando Restaurant: Usando sua classe Restaurant mais recente,
# armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
# Crie uma instância de Restaurant e chame um de seus métodos para mostrar que
# a instrução import funciona de forma apropriada

from restaurant import Restaurant

my_restaurant = Restaurant("Espetos_bar", "Espetinho e cerveja")
Restaurant.describe_restaurant(my_restaurant)
Restaurant.open_restaurant(my_restaurant)
