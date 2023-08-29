n = -1
a = 0
b = 1
while n <= 0:
    n = int(input("Digite um número inteiro maior que zero: "))
print(b)
for i in range(1, n):
    c = a + b
    print(c)
    a = b
    b = c
