n = -3
numero = 0
proxnumero = 1

while n <= 0:
    n = int(input("Insira um número inteiro maior que zero: "))
print(proxnumero)
for i in range(1, n):
    v = numero + proxnumero
    print(v)
    numero = proxnumero
    proxnumero = v