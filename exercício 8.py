# 8.	Escreva uma função que receba como parâmetro um valor n inteiro e positivo e que calcule a seguinte soma:
# S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n. A função deverá retornar o valor de S.


def parametro(n):
    s = 0
    if n > 0:
        for i in range(1, n + 1):
            s = s + 1/i

    return s

num = int(input('Digite um número: '))

resultado = parametro(num)
print(resultado)

# def calcular_soma(n):
#     soma = 0
#     for num in range(1, n+1):
#         soma = soma + 1/num
#     return soma
#
# numero = int(input("Digite um numero: "))
# if numero <= 0:
#     print("Numero invalido")
# else:
#     print(f"Soma = {calcular_soma(numero)}")