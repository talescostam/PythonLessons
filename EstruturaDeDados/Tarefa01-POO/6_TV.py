class TV:
    def __init__(self, canal=1, volume=1):
        self.canal: int = canal
        self.volume: int = volume

    def mudarCanal(self, novoCanal):
        self.canal = novoCanal

    def aumentarVolume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            return print('Volume já está no máximo.')

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            return print('Volume já está no mínimo.')
