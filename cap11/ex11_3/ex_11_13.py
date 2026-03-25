# 11.3 – Funcionário: Escreva uma classe chamada Employee. O método
# __init__() deve aceitar um primeiro nome, um sobrenome e um salário anual, e
# deve armazenar cada uma dessas informações como atributos. Escreva um método
# de nome give_raise() que some cinco mil dólares ao salário anual, por default,
# mas que também aceite um valor diferente de aumento.


class Employee:
    def __init__(self, first_name: str, surname: str, annual_wage: float):
        self.first_name = first_name
        self.surname = surname
        self.annual_wage = annual_wage

    def give_raise(self, increase: float = 5000):
        final_salary = self.annual_wage + increase

        return f"{self.first_name} {self.surname}, anuual wage = {self.annual_wage:.2f} + raise of R${increase:.2f} = R${final_salary:.2f}"
