def converter():
    n = input("Digite o algarismo romano: ")
    n0 = n
    dicionario = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = n.upper()
    resposta = 0
    for i in range(len(n)):
        x = i > 0 and dicionario[n[i]] > dicionario[n[i - 1]]
        if x:
            resposta += dicionario[n[i]] - 2 * dicionario[n[i - 1]]
        else:
            resposta += dicionario[n[i]]

    print(f"O número {n0} convertido em decimal é {resposta}")

converter()