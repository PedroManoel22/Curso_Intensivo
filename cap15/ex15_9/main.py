from pathlib import Path

import pygal
from die import Die

diretorio_atual = Path(__file__).parent
nome_arquivo = diretorio_atual / "main.svg"

# Cria dois dados D6
die_1 = Die()
die_2 = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results: list[int] = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analisa os resultados
frequencies: list[int] = []
max_result = die_1.num_sides * die_2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in range(2, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 * D6", frequencies)
hist.render_to_file(nome_arquivo)
