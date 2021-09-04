# 7.Escrever uma função somar_intervalo(n1, n2) que retorna a soma dos números inteiros que existem
# entre n1 e n2 (inclusive ambos). A função deve funcionar inclusive se o valor de n2 for menor que
# n1.  

def somar_intervalo(n1, n2):
    if n1 > n2:
        aux = n1
        n1 = n2
        n2 = aux

    soma = 0
    for i in range(n1, n2 + 1):
        soma = soma + i

    return soma



num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo  número:  '))

print(somar_intervalo(num1, num2))
