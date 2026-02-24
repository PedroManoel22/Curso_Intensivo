# 9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
# atributo privileges que armazene uma lista de strings conforme descrita no
# Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma
# instância de Privileges como um atributo da classe Admin. Crie uma nova
# instância de Admin e use seu método para exibir os privilégios.

from ex_9_7 import Admin
class Privileges(Admin):
    def __init__(self, *args):
        super().__init__()
        self.privileges_admin = self.privileges_admin
        self.privileges = args
        for a in self.privileges:
            self.privileges_admin.append(a)
    
    def show_privileges(self):
        return super().show_privileges()


new_privileges = Privileges('OI sou novo', 'ehhe', 'testando')
new_privileges.show_privileges()


    
        