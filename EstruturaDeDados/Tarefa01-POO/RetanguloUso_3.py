from Retangulo_3 import Retangulo_3

ladoA = int(input('Insira um dos lados do local em metros: '))
ladoB = int(input('Insira o outro lado do local em metros: '))

retangulo = Retangulo_3(ladoA, ladoB)

print(f'Você precisa de {retangulo.calcularPerimetro()} metros de rodapé.')
print(f'Você precisa de {retangulo.calcularArea()} metros² de piso.')
