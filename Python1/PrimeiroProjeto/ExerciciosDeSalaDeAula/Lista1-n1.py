# 1.	Elabore um programa em Python que leia a medida de um raio de um círculo e efetue o cálculo da sua área,
# exibindo o resultado ao final. (dica: use math.pi )
import math

raio = int(input("Digite o raio do círculo: "))
areaDoCirculo = math.pi * raio ** 2
print(f"A área do círculo é: {areaDoCirculo:2.2f}")
