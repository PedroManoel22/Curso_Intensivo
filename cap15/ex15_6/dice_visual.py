import pygal
from die import Die

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results: list[int] = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analisa os resultados
max_result = die_1.num_sides + die_2.num_sides

frequencies: list[int] = [results.count(value) for value in range(2, max_result + 1)]

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
