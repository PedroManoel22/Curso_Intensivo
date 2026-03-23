import json
from pathlib import Path

adress = Path(__file__).parent
filename = "number.json"
adress = adress / filename

with open(adress) as f_obj:
    number = json.load(f_obj)

print(f"Eu sei qual é o seu número favorito! É {number}.")
