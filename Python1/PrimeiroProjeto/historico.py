print("# 1)")
# "Crie um dicionário que catalogue as UCs que você está cursando neste semestre -
# as chaves devem ser o código da UC e os valores devem apenas ser o título da UC.
# Imprima o dicionário resultante.

modulo = {"1.1": "Introdução à Programação",
          "1.2": "Arquitetura de Computadores em Sistemas de Informação",
          "1.3": "Raciocínio Lógico e Matemático",
          "1.4": "Introdução a Redes de Computadores",
          "1.5": "Engenharia de Software I",
          "1.6": "Engenharia de Usabilidade",
          "1.7": "Tecnologia Web I",
          "1.8": "Responsabilidade Social - Extensão",
          "1.9": "Projeto Integrador 1"
          }

print(modulo)

print("")
print("# 2)")
# Altere os valores de cada chave, incluindo também a carga da UC. Imprima o dicionário resultante."

for chave in modulo:
    if chave != "1.1":
        modulo[chave] += " - 40h"
    else:
        modulo[chave] += " - 80h"

print(modulo)

print("")
print("# 3)")
# Em seguida, escreva uma função add_uc que receba 3 argumentos -
# um número de uc, uma descrição de uc com a carga e o dicionário - que adiciona novas UCs ao seu dicionário.
# Use esta função para adicionar as UCs que você fará no próximo semestre ao dicionário.


def add_uc(numero, descricao, carga):
    modulo[numero] = descricao + " - " + carga


add_uc("2.0", "Design de Interfaces", "40h")
add_uc("2.1", "Projeto Integrador II", "40h")
add_uc("2.2", "Estrutura de Dados", "80h")
add_uc("2.3", "Banco de Dados I", "40h")
add_uc("2.4", "Tecnologias Web II", "40h")
add_uc("2.5", "Programação I", "80h")
add_uc("2.6", "Engenharia de Software II", "80h")

print(modulo)

print(" ")
print("# 4)")


# Escreva uma função print_uc que receba dois argumentos - um número do módulo (por exemplo, '1')
# e o dicionário que você criou - e imprima todas as UCs que você fez nesse módulo.
# Certifique-se de que seu código funcione mesmo que você não tenha feito nenhuma aula nesse módulo!"


def print_uc(numeroDoModulo, dicionario):
    existe = False
    numeroDoModulo += "."
    for numeroUC, valor in dicionario.items():
        if numeroDoModulo in numeroUC:
            print(numeroUC + " " + valor)
            existe = True
    if not existe:
        print(f"Você não fez nenhuma aula no módulo {numeroDoModulo}")


print_uc("1", modulo)
print("")
print_uc("2", modulo)
print("")
print_uc("3", modulo)

print(" ")
print("# 5)")
# Escreva uma função carga_modulo que informe o total de carga horaria cumprida no módulo


def carga_modulo(numeroDoModulo, dicionario):
    valor_total = 0
    numeroDoModulo += "."
    for numeroUC, valor in dicionario.items():
        if numeroDoModulo in numeroUC:
            ultimos_3 = valor[-3:]
            dois_primeiros = ultimos_3[:2]
            valor_inteiro = int(dois_primeiros)
            valor_total += valor_inteiro
    print(f"A carga horário total cumprida no módulo é: {valor_total}h")


carga_modulo("1", modulo)
