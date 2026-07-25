import csv
from pathlib import Path

from matplotlib import pyplot as plt

ROOT_DIR = Path(__file__).parent
file_name = ROOT_DIR / "precipitacao_joao_pessoa_2025.csv"

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates: list[str] = []
    temps_max: list[int] = []
    temps_min: list[int] = []
    pre: list[int] = []

    for row in reader:
        try:
            date = row[0]
            _max = int(row[2])
            _min = int(row[1])
            _pre = int(row[3])

        except ValueError:
            print("valor inexistente!")

        else:
            dates.append(date)
            temps_max.append(_max)
            temps_min.append(_min)
            pre.append(_pre)


fig, ax1 = plt.subplots(figsize=(10, 6), dpi=128)

ax2 = ax1.twinx()  # type: ignore

bars = ax2.bar(dates, pre, color="#70a3e8", alpha=0.6, width=0.4, label="Preciptação")  # type: ignore

ax1.plot(  # type: ignore
    dates,
    temps_min,
    c="blue",
    alpha=0.5,
    marker="o",
    markersize=6,
    label="Temperatura mínima",
)  # type: ignore
ax1.plot(  # type: ignore
    temps_max, c="red", alpha=0.5, marker="o", markersize=6, label="Temperatura máxima"
)  # type: ignore
# ax.plot(pre, c="yellow", alpha=0.5, label="precipitation")


ax1.set_title(  # type: ignore[reportUnknownMemberType]
    "Climatologia e histórico de previsão do tempo em João Pessoa, BR", fontsize=20
)

ax1.set_xlabel("", fontsize=1)  # type: ignore[reportUnknownMemberType]
ax1.set_ylabel("Temperatura (C)", fontsize=16)  # type: ignore[reportUnknownMemberType]
ax2.set_ylabel("Preciptaçãp (mm)", fontsize=16)  # type: ignore[reportUnknownMemberType]
ax1.tick_params(axis="both", which="major", labelsize=16)  # type: ignore[reportUnknownMemberType]
# Pega os handles (desenhos) e labels do ax1 e do ax2
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

# Cria a legenda unificada com os elementos de ambos
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, fontsize=10)  # type: ignore
fig.autofmt_xdate()

print(temps_min)

plt.show()  # type: ignore
