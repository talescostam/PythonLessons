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


adicional = 0
idade = int(input("insira sua idade :"))
if idade <= 10:
    adicional = 60.00
elif 10 < idade <= 30:
    adicional = 90.00
elif 30 < idade <= 45:
    adicional = 130.00
elif 45 < idade <= 59:
    adicional = 250.00
elif idade > 60:
    adicional = 400.00

valorDoPlano = 100.00 + adicional

print(f"Valor final a ser pago com a idade {idade} é : {valorDoPlano:.2f}")
