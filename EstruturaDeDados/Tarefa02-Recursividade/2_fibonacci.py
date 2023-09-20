# 2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci.
# Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

numero = 12
soma = 0
numeroAnterior = 0
numeroSeguinte = 1
for i in range(numero-2):
    soma = numeroAnterior + numeroSeguinte
    numeroAnterior = numeroSeguinte
    numeroSeguinte = soma

print(soma)
