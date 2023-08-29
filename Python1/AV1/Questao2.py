a = -1
b = 0
c = -43908752908375809237509823709582473
while a <= 0 or b <= 0 or c <= 0:
    a = int(input("insira um valor do cateto 1: "))
    b = int(input("insira um valor do cateto 2: "))
    c = int(input("insira um valor da hipotenusa: "))
if (a**2 + b**2)**(1/2) == c:
    print(f"Os lados {a},{b} e {c} formam um Triangulo retângulo.")
else:
    print(f"Os lados {a},{b} e {c} NÃÃÃÃO formam um Triangulo retângulo, PORRA.")
