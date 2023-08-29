import math
a = -1
b = -1
c = -1

while a < 0 or b < 0 or c < 0:
    a = int(input("Insira o valor do lado 'a' do triângulo: "))
    b = int(input("Insira o valor do lado 'b' do triângulo: "))
    c = int(input("Insira o valor do lado 'c' do triângulo: "))

if math.sqrt(a**2 + b**2) == c:
    print(f"Os lados {a}, {b} e {c} formam um Triangulo retângulo.")
else:
    print(f"Os lados {a}, {b} e {c} Não formam um Triangulo retângulo.")
