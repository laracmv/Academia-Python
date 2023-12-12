import math

def desviopadrao(vd,mediavd):
    part1 = 1/(len(vd) - 1)
    i = 0
    somatorio = 0
    while i < len(vd):
        somatorio+= (vd[i] - mediavd)**2
        i +=1
    desvio = math.sqrt(part1 * somatorio)
    return desvio

lista = [2,2,5,7]
media = 4
print(desviopadrao(lista, media))