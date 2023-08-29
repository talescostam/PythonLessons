class Ponto:
    def __init__(self, nome, x, y):
        self.nome: str = nome
        self.x: int = x
        self.y: int = y

    def __str__(self):
        return f"{self.nome}:({self.x},{self.y})"


