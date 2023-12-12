# Faça uma função que recebe como entrada um número inteiro e testa a divisibilidade por 2 e 3.

# Se for divisível por 2, sua função deve retornar a string "Ins". Se for por 3, retorna "per". Porém, se for por 2 e 3 ao mesmo tempo retorna "Insper". Para outros casos, sua função deve devolver o próprio número.

# O nome da sua função deve ser divisivel

def divisivel(n):
    if n%2 == 0 and n%3 == 0:
        return "Insper"
    elif n%3 ==0:
        return "per"
    elif n % 2 == 0:
        return "Ins"
    else:
        return (n)