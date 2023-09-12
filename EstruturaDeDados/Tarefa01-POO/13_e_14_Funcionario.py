class Funcionario:
    def __init__(self, nome, salario):
        self.nome: str = nome
        self.salario: float = salario

    def getNome(self):
        return print(f'Nome: {self.nome}')

    def getSalario(self):
        return print(f'Salário: US$ {self.salario}')

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento/100)


tales = Funcionario("Tales Costa", 25000.00)
tales.getNome()
tales.getSalario()
tales.aumentarSalario(10)
tales.getSalario()
