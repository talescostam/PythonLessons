n = int(input("Digite um número inteiro: "))
divisor = 1
while divisor <= n:
    if n % divisor == 0:
        print(divisor)
    divisor += 1
