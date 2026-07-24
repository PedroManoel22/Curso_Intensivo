import csv
from datetime import datetime, timezone
from pathlib import Path

from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas do arquivo
root_dir = Path(__file__).parent
filename = root_dir / "sitka_weather_2021_full.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pegando as temperaturas máxiams de cada dia
    dates: list[datetime] = []
    highs: list[int] = []
    lows: list[int] = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )

            high = int(row[7])
            low = int(row[8])

        except ValueError:
            pass

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))  # Tamanho da janela
plt.plot(dates, highs, c="red", alpha=0.5)  # alpha é a transparência da linha
plt.plot(dates, lows, c="blue", alpha=0.5)  # alpha é a transparência da linha
plt.fill_between(
    dates, highs, lows, facecolor="blue", alpha=0.1
)  # Preenche a área entre as linhas

plt.title(
    "Temperaturas Máximas e Mínimas Diárias, 10 primeiros dias - 2021", fontsize=20
)
plt.xlabel("", fontsize=1)
fig.autofmt_xdate()  # Formata as datas para não sobrepor
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
