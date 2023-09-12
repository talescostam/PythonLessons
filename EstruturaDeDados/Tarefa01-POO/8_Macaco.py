class Macaco:
    def __init__(self, nome, bucho=None):
        if bucho is None:
            bucho = []
        self.nome: str = nome
        self.bucho: list = bucho

    def comer(self, comida):
        if isinstance(comida, Macaco):
            self.bucho.append(comida.nome)
            return print(f'O macaco {self.nome} É UM CANIBAL e está comendo {comida.nome}...')
        else:
            self.bucho.append(comida)
            return print(f'O macaco {self.nome} está comendo {comida}...')

    def digerir(self, comida):
        if comida in self.bucho:
            self.bucho.remove(comida)
            return print(f'O macaco {self.nome} está digerindo {comida}...')

    def verBucho(self):
        if len(self.bucho) == 0:
            buchoAtual = "fome kkkk"
        else:
            buchoAtual = self.bucho
        return print(f'Dentro do estômago do macaco {self.nome} tem: {buchoAtual}')


macaco1 = Macaco("Tião")
kingKong = Macaco("King Kong")

macaco1.verBucho()
macaco1.comer("banana")
macaco1.verBucho()
macaco1.digerir("banana")
macaco1.verBucho()

kingKong.verBucho()
kingKong.comer(macaco1)
kingKong.verBucho()
