# Faça um programa que leia dois valores representando a base e o expoente de uma potência.
# Você deve implementar uma função que computa a potência ab para valores a e b
# (assuma números inteiros) passados por parâmetro.
# Obs.: Não use o operador ** nem funções de potência da biblioteca.

def potencia():
    a = int(input("Insira o valor da base: "))
    b = int(input("Insira o valor do expoente: "))
    resposta = a
    if b == 0:
        print(1)
    else:
        for i in range(b - 1):
            resposta *= a
        print(resposta)


potencia()
