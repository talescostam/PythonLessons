# 4.	Faça um programa que calcule o fatorial de um número positivo informado pelo usuário.
x = -1
while x < 0:
    x = int(input("Digite um número positivo: "))
    if x < 0:
        print("Número inválido. Tente novamente.")
    else:
        print("Número válido!")
fatorial = 1
for i in range(1, x+1):
    fatorial *= i
print(f"O fatorial de {x} é: {fatorial}")
