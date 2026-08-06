from pathlib import Path
from typing import Any

import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

ROOT_DIR = Path(__file__).parent
FILE_NAME = "python_repos.svg"
FILE_DIR = ROOT_DIR / FILE_NAME

# Faz uma chamada de API e armazena a resposta
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Armazena a resposta da API em uma variável
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# Explora informações sobre os repositórios
repo_dicts = response_dict["items"]

names: list[str] = []
plot_dicts: list[dict[str, Any]] = []

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict: dict[str, Any] = {
        "value": repo_dict["stargazers_count"],
        "label": str(repo_dict["description"]),
        "xlink": repo_dict["html_url"],
    }

    plot_dicts.append(plot_dict)

# Cria a visualização
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config(
    x_label_rotation=45,
    show_legend=False,
    title_font_size=24,
    label_font_size=14,
    major_label_font_size=18,
    truncate_label=15,
    show_y_guides=False,
    width=1000,
)


chart = pygal.Bar(my_config, style=my_style)

chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", plot_dicts)  # type: ignore
chart.render_to_file(FILE_DIR)  # type: ignore
