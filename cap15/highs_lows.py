import csv
from pathlib import Path

from matplotlib import pyplot as plt

root_dir = Path(__file__).parent
filename = root_dir / "sitka_weather_2021_full.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pegando as temperaturas máxiams de cada d
    highs: list[int] = []
    for row in reader:
        try:
            high = int(row[7])
            highs.append(high)
        except ValueError:
            pass

fig = plt.figure(dpi=128, figsize=(10, 6))  # Tamanho da janela
plt.plot(highs, c="red")

plt.title("Temperaturas Máximas Diárias - 2021", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
