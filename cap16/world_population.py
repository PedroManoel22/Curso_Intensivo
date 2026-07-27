import json
from pathlib import Path

root_dir = Path(__file__).parent
filename = "population_data.json"
filedir = root_dir / filename

# Carrega os dados em uma lista

with open(filedir) as f:
    pop_data = json.load(f)

# Exibe a população de cada país em 2010

for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = pop_dict["Value"]
        print(country_name + ": " + population)
