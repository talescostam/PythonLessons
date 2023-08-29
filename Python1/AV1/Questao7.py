n = -3
numeroAnterior = 0
umNumero = 1
while n <= 0:
    n = int(input("Digite um número inteiro maior que zero: "))
print(umNumero)
for i in range(1, n):
    proximoNumero = numeroAnterior + umNumero
    print(proximoNumero)
    numeroAnterior = umNumero
    umNumero = proximoNumero
