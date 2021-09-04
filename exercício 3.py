# 3.	Faça uma função que recebe por parâmetro o raio de uma esfera
# e calcule o seu volume (v = (4 x pi x R3)/3).  

def parametro(r):
    v = (4 * 3.14 * r**3) / 3
    return v


print('calculo do volume da esfera')
raio = float(input("Digite o raio da esfera: "))
resultado = parametro(raio)
print(f'Raio = {resultado:.2f}')