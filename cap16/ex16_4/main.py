import csv
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

dados: list[float] = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]


for mes in range(1, 7):
    ROOT_DIR = Path(__file__).parent
    filename = f"dados_mes{mes}.csv"
    file_dir = ROOT_DIR / "dados" / filename

    radiacao: list[float] = []

    with open(file_dir) as f:
        reader = csv.reader(f, delimiter=";")
        header_now = next(reader)

        for row in reader:
            if row[1] != " ":
                valor_limpo = row[1].replace(",", ".").strip()
                radiacao.append(float(valor_limpo))

        media = round(float(np.mean(radiacao)), 2)
        dados.append(media)

        radiacao = []


fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

ax.plot(meses, dados, c="blue", alpha=0.5, marker="o", markersize=5)  # type: ignore[reportUnknownMemberType]
ax.set_title("Médias de radiação global dos meses 01 a 06", fontsize=20)  # type: ignore[reportUnknownMemberType]
ax.set_xlabel("", fontsize=1)  # type: ignore[reportUnknownMemberType]
ax.set_ylabel("RADIACAO GLOBAL (Kj/m²)", fontsize=16)  # type: ignore[reportUnknownMemberType]
ax.tick_params(axis="both", which="major", labelsize=16)  # type: ignore[reportUnknownMemberType]

fig.autofmt_xdate()

plt.show()  # type: ignore[reportUnknownMemberType]
