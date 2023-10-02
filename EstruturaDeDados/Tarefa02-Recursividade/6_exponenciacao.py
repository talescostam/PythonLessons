#Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n .
# Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n
# e imprimir o resultado da chamada da função.
def potenciacao(k, n):
    if n == 0:
        return 1
    else:
        return k * potenciacao(k, n - 1)

k = int(input("Valor de k: "))
n = int(input("Valor de n: "))

x = potenciacao(k, n)

print(f"{k}^{n} = {x}")
