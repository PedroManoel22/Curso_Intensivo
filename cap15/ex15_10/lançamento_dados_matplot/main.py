from pathlib import Path

import matplotlib.pyplot as plt
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
# Defini o tamanho da janela de pltagem
plt.figure(dpi=128, figsize=(10, 6))

x_values = list(range(2, max_result + 1))
plt.bar(x_values, frequencies, width=0.8)
plt.xlabel("Result")
plt.ylabel("Frequencies of Results")
plt.title("Results of rolling two D6 dice 1000 times")

# Salvar o gráfico
plt.savefig(nome_arquivo, bbox_inches="tight")
