# 6.	Elaborar um programa que solicita a entrada de 3 valores (a, b, c)
# e verifica se esses valores podem formar ou não um triângulo.
# Você deve considerar que os valores lidos são inteiros e positivos.
# Caso os valores formem um triângulo, exiba essa informação e o valor do perímetro deste triângulo.
# Se não formarem triângulo, apenas exiba uma mensagem com essa informação.
# (Obs.: Para formar um triângulo, cada suposto lado deve ser menor do que a soma dos outros dois lados.)

a = -1
b = -1
c = -1
while a < 0 or b < 0 or c < 0:
    a = int(input("insira o 1º valor inteiro e positivo: "))
    b = int(input("insira o 2º valor inteiro e positivo: "))
    c = int(input("insira o 3º valor inteiro e positivo: "))

    if a < 0 or b < 0 or c < 0:
        print("Pelo menos um número é inválido. Tente novamente.")
    else:
        print("Números válidos!")

if a > b + c or b > a + c or c > a + b:
    print("Não podem formar um triângulo.")
else:
    print(f"Os valores {a}, {b} e {c} podem formar um triângulo com o perímetro de {a + b + c}.")
