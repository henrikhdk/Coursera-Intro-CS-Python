num = int(input("Digite o número a ser calculado "))

soma = 0

while (num != 0):
    sobra = num % 10
    num = (num - sobra) // 10
    soma = soma + sobra
print(soma)