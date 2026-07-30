import json
from pathlib import Path

import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import LightColorizedStyle as LCS
from pygal.style import RotateStyle as RS

root_dir = Path(__file__).parent.parent
filename = "population_data.json"
filedir = root_dir / filename

# Carrega os dados em uma lista

with open(filedir) as f:
    pop_data = json.load(f)

# Constrói um dicionário com dados das populações
cc_populations = {}
faltantes = {}


for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            faltantes[country_name] = population


faltantes_2_codes = {}

for k, v in faltantes.items():
    if len(k.split()) == 2:
        faltantes_2_codes[k] = v

# Paises que não tem codigos
lista_exclusao = [
    "Arab World",
    "Euro area",
    "High income",
    "Low income",
    "Middle income",
    "North America",
    "OECD members",
    "Small states",
    "South Asia",
]

# Exluindo países que não foram computados e que não tem códigos de duas letras
faltantes_2_codes = [
    {name: population}
    for name, population in faltantes_2_codes.items()
    if name not in lista_exclusao
]

faltantes_codes = [
    "EU",
    "AS",
    "BS",
    "KY",
    "GG",
    "CG",
    "FO",
    "PF",
    "GM",
    "KR",
    "KG",
    "LA",
    "MK",
    "MH",
    "NC",
    "SK",
    "SB",
    "LC",
    "VE",
    "YE",
]

# Criamos um novo dicionário combinando o código e a população
populacoes_faltantes = {}

for code, f in zip(faltantes_codes, faltantes_2_codes):
    for pop in f.values():
        populacoes_faltantes[code] = pop

cc_populations = cc_populations | populacoes_faltantes


# Agrupa os países em três níveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Vê quantos países estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS("#336699", base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops_1)
wm.add("10m-1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)

wm.render_to_file("world_population_ex_16_5.svg")
