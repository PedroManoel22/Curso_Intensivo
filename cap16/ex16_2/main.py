# Como eu não conseguir achar os dados de sitka em 2014 ficamos com os dados de sitka e death valley em 2021

import csv
from datetime import datetime, timezone
from pathlib import Path

from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas do arquivo
root_dir = Path(__file__).parent.parent

filename_stika = root_dir / "sitka_weather_2021_full.csv"
filename_death = root_dir / "death_valley_2021_full.csv"


# ler arquivo stika
with open(filename_stika) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pegando as temperaturas máxiams de cada dia
    dates: list[datetime] = []
    highs: list[float] = []
    lows: list[float] = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )

            high = float(row[7])
            low = float(row[8])

        except ValueError:
            print(current_date, "missing data")  # type: ignore[reportUnknownMemberType]

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# ler arquivo death
with open(filename_death) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pegando as temperaturas máxiams de cada dia
    dates_death: list[datetime] = []
    highs_death: list[int] = []
    lows_death: list[int] = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )

            high = int(row[6])
            low = int(row[7])

        except ValueError:
            print(current_date, "missing data")  # type: ignore[reportUnknownMemberType]

        else:
            dates_death.append(current_date)
            highs_death.append(high)
            lows_death.append(low)

fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

ax.plot(dates, highs, c="red", alpha=0.5, label="Maximum Sitka")  # type: ignore[reportUnknownMemberType]
ax.plot(dates, lows, c="blue", alpha=0.5, label="Minimum Sitka")  # type: ignore[reportUnknownMemberType]
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # type: ignore[reportUnknownMemberType]

ax.plot(dates_death, highs_death, c="yellow", alpha=0.5, label="Maximum Death")  # type: ignore[reportUnknownMemberType]
ax.plot(dates_death, lows_death, c="black", alpha=0.5, label="Minimum Death")  # type: ignore[reportUnknownMemberType]
ax.fill_between(dates_death, highs_death, lows_death, facecolor="blue", alpha=0.1)  # type: ignore[reportUnknownMemberType]

ax.set_title(  # type: ignore[reportUnknownMemberType]
    "Daily high and low temperatures - 2021\nStika / Death Valley", fontsize=20
)
ax.set_xlabel("", fontsize=1)  # type: ignore[reportUnknownMemberType]
ax.set_ylabel("Temperatura (F)", fontsize=16)  # type: ignore[reportUnknownMemberType]
ax.tick_params(axis="both", which="major", labelsize=16)  # type: ignore[reportUnknownMemberType]
ax.legend(fontsize=10)  # type: ignore
fig.autofmt_xdate()

plt.show()  # type: ignore[reportUnknownMemberType]
