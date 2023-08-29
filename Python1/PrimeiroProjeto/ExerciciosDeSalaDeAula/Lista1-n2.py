# 2.	Escreva um programa que imprima os 100 primeiros números ímpares.
contador = 0
x = 0
while contador < 100:
    if x % 2 != 0:
        print(x)
        contador += 1
    x += 1
