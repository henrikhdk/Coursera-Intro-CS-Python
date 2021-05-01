import math

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é:", raiz1)

else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A primeira raiz é:", raiz1)
        print("A segunda raiz é:", raiz2)


'''
se delta for menor que zero = Está equação não possui raizes reais
se detal for igual a zero = A raiz desta equação é VALOR DA RAIZ
se o delta for maior que zero = As raizes da equação são PRIMEIRA RAIZ e SEGUNDA RAIZ
'''