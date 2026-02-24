# 4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de
# comida. Pense em cinco pratos simples e armazene-os em uma tupla.
# • Use um laço for para exibir cada prato oferecido pelo restaurante.
# • Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
# • O restaurante muda seu cardápio, substituindo dois dos itens com pratos
# diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
# use um laço for para exibir cada um dos itens do cardápio revisado.
from rich.panel import Panel
from rich import print

buffet = (
    "Macarrão simples",
    "macarrão completo",
    "Mini pizza",
    "Camarão frito",
    "Fritas",
)

buffet_formatado = "\n".join(buffet)
menu = Panel(f"{buffet_formatado}", title="Menu Buffet", width=30)
print(menu)

# buffet[1] = 'Qualquer prato'

buffet = (
    "Escondidinho",
    "macarrão completo",
    "Mini pizza",
    "Camarão frito",
    "Galinha caipira",
)
print("\n")
buffet_formatado = "\n".join(buffet)
menu = Panel(f"{buffet_formatado}", title="Menu Buffet", width=30)
print(menu)
