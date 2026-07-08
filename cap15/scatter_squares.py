from pathlib import Path

import matplotlib.pyplot as plt

diretorio_atual = Path(__file__).parent
caminho_salvamento = diretorio_atual / "squares_plt.png"

# pyright: reportUnknownMemberType=false

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none", s=40)

# Define o título do gráfico e nomeia os eixos

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])  # type: ignore

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

# Salvando o gráfico em um arquivo png (Lembre-se de sempre salvar antes de exibir)
plt.savefig(
    caminho_salvamento, bbox_inches="tight"
)  # segundo argumento remove espaços em branco ao redor do gráfico


plt.show()
