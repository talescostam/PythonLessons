import math

a = int(input("Insira o valor de um cateto do triângulo: "))
b = int(input("Insira o valor de outro cateto do triângulo: "))
c = math.sqrt(a**2 + b**2)
print(f"A hipotenusa de um triângulo retângulo de lados {a} e {b} é: {c:.1f}")
