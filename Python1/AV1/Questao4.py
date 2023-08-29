idade = 0
contadorDeQuantidadeDeIdade = 0
somaDeIdade = 0

while idade >= 0:
    idade = int(input("Diga uma idade: "))
    if idade >= 0:
        contadorDeQuantidadeDeIdade += 1
        somaDeIdade += idade

media = somaDeIdade / contadorDeQuantidadeDeIdade
print(f"A média aritmética dessas idade é: {media:.2f}")
