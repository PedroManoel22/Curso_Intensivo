import matplotlib.pyplot as plt

# pyright: reportUnknownMemberType=false

# Plotando os 5 primeiros números ao cubo

numeros = list(range(1, 6))
numeros_ao_cubo = [x**3 for x in numeros]
plt.scatter(
    numeros,
    numeros_ao_cubo,
    c="black",
    edgecolors="none",
    s=40,
)

# Define o título do gráfico e nomeia os eixos
plt.title("Números ao cubo (5 primeiros)", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Valor ao cubo", fontsize=14)

plt.show()


# Plotando os 5000 primeiros números ao cubo

numeros = list(range(1, 5001))
numeros_ao_cubo = [x**3 for x in numeros]
plt.scatter(
    numeros,
    numeros_ao_cubo,
    c="blue",
    edgecolors="none",
    s=40,
)

# Define o título do gráfico e nomeia os eixos
plt.title("Números ao cubo (5000 primeiros)", fontsize=24)
plt.xlabel("Valor", fontsize=14)
plt.ylabel("Valor ao cubo", fontsize=14)

plt.show()
