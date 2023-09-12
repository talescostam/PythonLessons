class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome: str = nome
        self.idade: int = idade
        self.peso: float = peso
        self.altura: float = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura
