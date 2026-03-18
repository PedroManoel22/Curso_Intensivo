# 9.11 – Importando Admin: Comece com seu programa do Exercício 9.8 (página
# 241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
# arquivo separado e uma instância de Admin e chame show_privileges() para
# mostrar que tudo está funcionando de forma apropriada

from modules import Admin

adm = Admin()
adm.describe_user()
adm.show_privileges()
