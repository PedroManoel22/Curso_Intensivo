from pathlib import Path

import pygal
from die import Die

diretorio = Path(__file__).parent
nome_arquivo = "main.svg"
diretorio_arquivo = diretorio / nome_arquivo


die1 = Die(8)
die2 = Die(8)

results: list[int] = [die1.roll() + die2.roll() for _ in range(100000)]

max_result = die1.num_sides + die2.num_sides

frequencies: list[int] = [results.count(value) for value in range(2, max_result + 1)]

hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]

hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6", frequencies)
hist.render_to_file(diretorio_arquivo)
