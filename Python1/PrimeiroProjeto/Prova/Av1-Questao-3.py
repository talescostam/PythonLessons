n = 1001
while n > 1000:
    n = int(input("Insira um número inteiro menor que 1000: "))
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)
