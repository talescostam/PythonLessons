# 3.	Escreva um programa que imprima todos os números pares
# compreendidos entre 85 e 907. O programa deve também calcular a
# soma destes valores
soma = 0
for x in range(85, 907):
    if x % 2 == 0:
        soma = soma + x
        print(x)
print(soma)
