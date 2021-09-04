# 6.Escrever uma função calcular_quociente(dividendo, divisor),
# que  retorna a divisão inteira (sem casas decimais) de dividendo por divisor
# e outra função  calcular_resto(dividendo, divisor) que retorna o resto.

def calcular_conciente(dividendo, divisor):
    return dividendo // divisor


def calcular_resto(dividendo, divisor):
    return dividendo % divisor

dividendo = float(input('Digite o número ao qual quer dividir: '))
divisor = float(input('Divisor: '))

divisao = calcular_conciente(dividendo, divisor)
resto = calcular_resto(dividendo, divisor)

print(f'divisão inteira = {divisao}, resto = {resto}')