notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
print(sum(notas))

notas.insert(1, 5.0)
print(notas)

notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
notas.remove(7.0)
print(notas)

notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
print('a maior nota é: ', max(notas))
print('a menor nota é: ', min(notas))

notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
notas.sort()
print(notas)

animais = ['gato', 'tatu', 'rato', 'pato']
sorted(animais)
print(animais)
print(sorted(animais))

notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
print(notas)

print(sorted(notas))
print(notas)

animais = ['gato', 'tatu', 'rato', 'pato']
notas = [0, 10.0, 7.0, 7.0, 8.0, 8.0]
notas.extend(animais)
print(notas)
print(animais)

exemplo = ['z', 'y'] + ['x',]
print(exemplo)

exemplo = ['z', 'y'] + ['x']
print(exemplo)

exemplo += [3,]
print(exemplo)

exemplo * 2
print(exemplo*2)

exemplo *= 2
print(exemplo)
print(exemplo*3)
