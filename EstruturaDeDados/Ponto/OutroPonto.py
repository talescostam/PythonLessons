from Ponto import Ponto


class OutroPonto:
    pontos_por_tipo = {}

    with open("C:\Users\psyta\PycharmProjects\PythonLessons\EstruturaDeDados\Ponto\pontos.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    i = 0
    while i < len(linhas):
        nome = linhas[i].strip()
        x, y = map(int, linhas[i + 1].strip().split())

        if nome not in pontos_por_tipo:
            pontos_por_tipo[nome] = []

        pontos_por_tipo[nome].append(Ponto(nome, x, y))

        i += 2

    for tipo, lista in pontos_por_tipo.items():
        for ponto in lista:
            print(ponto)
        print()
