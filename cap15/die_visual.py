import pygal
from die import Die

# Cria um dado de seis lados
die1 = Die()

# Faz alguns lançamentos e armazena os resultados numa lista
results: list[int] = []

for roll_num in range(1000):
    result = die1.roll()
    results.append(result)

# Analisa os resultados
frequences: list[int] = []
max_result = die1.num_sides

for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequences.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()

hist.title = "Resultados de 1000 lançamentos de um dado de seis lados"
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist.x_title = "Resultado"
hist.y_title = "Frequência de cada resultado"

hist.add("D6", frequences)
hist.render_to_file("die_visual.svg")
