# 2.Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito,
# conforme a tabela abaixo:  

def conceito(nota):
    if nota >= 0 and nota < 50:
        nota = 'D'
    else:
        if nota >= 50 and nota < 70:
            nota = 'C'
        else:
            if nota >= 70 and nota < 90:
                nota = 'B'
            else:
                if nota >= 90 and nota <= 100:
                    nota = 'A'
                else:
                    nota = 'inválido'
    return nota



notascavalo = float(input("Digite a média final: "))

print(f'conceito da nota = {conceito(notascavalo)}')