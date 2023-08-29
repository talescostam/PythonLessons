class Automovel:

    def __init__(self, placa):
        print("Executando o construtor...")
        self.__placa = None
        self.set_placa(placa)

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if len(placa) < 5:
            print('A placa não tem dígitos suficientes')
        else:
            self.__placa = placa

    def dirigir(self, velocidade):
        print(f'estou dirigindo a {velocidade} km/h ')


corola = Automovel('RJ123')
fusca = Automovel("SP123")
corsa = Automovel("AM12")

print(corola.get_placa())
print(fusca.get_placa())
print(corsa.get_placa())

corsa.set_placa("A")

print(corsa.get_placa())
