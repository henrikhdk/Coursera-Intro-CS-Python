'''
Exercício 5 - Verificando ordenação
Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima 

não está em ordem crescente
'''

a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if a < b < c:
    print('crescente')
else:
    print('não está em ordem crescente')