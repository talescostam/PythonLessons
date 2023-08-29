# 5.	Uma seguradora de saúde está oferecendo um plano de saúde promocional em que
# todos os conveniados pagam R$ 100,00 mais um adicional, de acordo com sua idade.
# As regras para esse adicional seguem a tabela abaixo:
# ____________________________________________
#           Idade               Adicional (R$)
# <= 10 anos                    60,00
# Entre 10 e 30 (incluindo 30)  90,00
# Entre 30 e 45 (incluindo 45)  130,00
# Entre 45 e 59 (incluindo 59)  250,00
# A partir de 60                400,00
# ____________________________________________
# O programa deve permitir que o usuário informe sua idade
# e deve exibir o valor final a ser pago pelo plano contratado.
adicional = 0
idade = int(input("insira sua idade :"))
if idade <= 10:
    adicional = 60.00
elif 10 < idade <= 30:
    adicional = 90.00
elif 30 < idade <= 45:
    adicional = 130.00
elif 45 < idade <= 59:
    adicional = 250.00
elif idade > 60:
    adicional = 400.00

valorDoPlano = 100.00 + adicional

print(f"Valor final a ser pago com a idade {idade} é : {valorDoPlano:.2f}")
