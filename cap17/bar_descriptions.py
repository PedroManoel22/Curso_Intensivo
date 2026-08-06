from pathlib import Path

import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

ROOT_DIR = Path(__file__).parent
FILE_NAME = "bar_descriptions.svg"
FILE_DIR = ROOT_DIR / FILE_NAME


my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = "Python Projects"
chart.x_labels = ["httpie", "django", "flask"]

plot_dicts: list[dict[str, int | str]] = [
    {"value": 16101, "label": "Description of httpie."},
    {"value": 15028, "label": "Description of django."},
    {"value": 14798, "label": "Description of flask."},
]

chart.add("", plot_dicts)  # type: ignore
chart.render_to_file(FILE_DIR)  # type: ignore
