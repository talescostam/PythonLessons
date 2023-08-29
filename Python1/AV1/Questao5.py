n = int(input("insira o valor de N: "))
divisor = 1
while divisor <= n:
    if n % divisor == 0:
        print(divisor)
    divisor = divisor + 1
