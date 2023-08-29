print("Combustível    Código")
print("Gasolina       1")
print("Álcool         2")
print("Diesel         3")
print("Fim            4")
print("")
codigoDoCombustivel = 0
contadorDeGasolina = 0
contadorDeAlcool = 0
contadorDeDiesel = 0
while codigoDoCombustivel != 1 or codigoDoCombustivel != 2 or codigoDoCombustivel != 3 or codigoDoCombustivel != 4:
    codigoDoCombustivel = int(input("Insira o código do combustível escolhido: "))
    if codigoDoCombustivel == 1:
        contadorDeGasolina += 1
    elif codigoDoCombustivel == 2:
        contadorDeAlcool += 1
    elif codigoDoCombustivel == 3:
        contadorDeDiesel += 1
    elif codigoDoCombustivel == 4:
        print("MUITO OBRIGADO")
        print(f"Gasolina: {contadorDeGasolina}")
        print(f"Alcool: {contadorDeAlcool}")
        print(f"Diesel: {contadorDeDiesel}")
        break
