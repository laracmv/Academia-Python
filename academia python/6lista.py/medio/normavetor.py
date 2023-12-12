import math

def calcula_norma(vetor):
    i = 0
    soma = 0
    while i < len(vetor):
        soma += vetor[i]**2
        i+=1
    v = math.sqrt(soma)
    return v