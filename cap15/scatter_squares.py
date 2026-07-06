import matplotlib.pyplot as plt

# pyright: reportUnknownMemberType=false

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=(0.84, 0.37, 0.00), edgecolors="none", s=40)

# Define o título do gráfico e nomeia os eixos

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])  # type: ignore

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
