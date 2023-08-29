class Veiculo:
    def __init__(self, motor, rodas):
        self.motor: str = motor
        self.rodas: int = rodas

    def andar(self):
        return "Andando."

    def __str__(self):
        return f"Motor: {self.motor}, Rodas: {self.rodas}"


class VeiculoMotorizado(Veiculo):
    def __init__(self, rodas):
        super().__init__("sim", rodas)
        self.acelerar()

    def acelerar(self):
        return "Acelerando."


class VeiculoSemMotor(Veiculo):
    def __init__(self, rodas):
        super().__init__("não", rodas)


class VeiculoDe2Rodas(Veiculo):
    def __init__(self, motor):
        super().__init__(motor, 2)


class VeiculoDe4Rodas(Veiculo):
    def __init__(self, motor):
        super().__init__(motor, 4)


class VeiculoDeMaisDe4Rodas(Veiculo):
    def __init__(self, motor):
        super().__init__(motor, 6)


class Bicicleta(VeiculoSemMotor, VeiculoDe2Rodas):
    def __init__(self):
        VeiculoSemMotor.__init__(self, 2)
        VeiculoDe2Rodas.__init__(self, "não")
        self.pedalar()

    def pedalar(self):
        return "Pedalando."


class Moto(Veiculo, VeiculoMotorizado, VeiculoDe2Rodas):
    pass


class Carro(Veiculo, VeiculoMotorizado, VeiculoDe4Rodas):
    pass


class Camionete(Veiculo, VeiculoMotorizado, VeiculoDe4Rodas):
    def __init__(self):
        self.transportar()

    def transportar(self):
        return "Transportando."


class Caminhao(Veiculo, VeiculoMotorizado, VeiculoDeMaisDe4Rodas, Camionete):
    pass


bicicleta = Bicicleta()
moto = Moto()
carro = Carro()
camionete = Camionete()
caminhao = Caminhao()

print(bicicleta)
print(moto)
print(carro)
print(camionete)
print(caminhao)
