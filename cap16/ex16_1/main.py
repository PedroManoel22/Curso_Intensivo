import csv
from datetime import datetime, timezone
from pathlib import Path

from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas do arquivo
root_dir = Path(__file__).parent.parent

print(root_dir)

filename = root_dir / "san_francisco_weather_2014.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pegando as temperaturas máxiams de cada dia
    dates: list[datetime] = []
    highs: list[float] = []
    lows: list[float] = []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )

            high = float(row[1])
            low = float(row[2])

        except ValueError:
            print(current_date, "missing data")  # type: ignore[reportUnknownMemberType]

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

ax.plot(dates, highs, c="red", alpha=0.5)  # type: ignore[reportUnknownMemberType]
ax.plot(dates, lows, c="blue", alpha=0.5)  # type: ignore[reportUnknownMemberType]
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # type: ignore[reportUnknownMemberType]

ax.set_title("Daily high and low temperatures - 2014\nSan Fracisco", fontsize=20)  # type: ignore[reportUnknownMemberType]
ax.set_xlabel("", fontsize=1)  # type: ignore[reportUnknownMemberType]
ax.set_ylabel("Temperatura (F)", fontsize=16)  # type: ignore[reportUnknownMemberType]
ax.tick_params(axis="both", which="major", labelsize=16)  # type: ignore[reportUnknownMemberType]

fig.autofmt_xdate()

plt.show()  # type: ignore[reportUnknownMemberType]
