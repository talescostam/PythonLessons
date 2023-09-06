dic = {'a': 1, 'b': 2, 'c': 3}
dicionario = {'letra1': 'a', 'letra2': 'b', 'letra3': 'c'}

print(dicionario)

dicionario.update()

print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())

for k, v in dicionario.items():
    print("chave: ", k)
    print("valor: ", v)