def encontra_maximo(lista):
    maior = lista[0][0]
    i = 0
    f = 0
    g = 0
    while i < len(lista[0]):
        if abs(lista[0][i]) > abs(maior):
            maior = lista[0][i]
        i+=1
    while f < len(lista[1]):
        if abs(lista[1][f]) > abs(maior):
            maior = lista[1][f]
        f+=1
    while g < len(lista[2]):
        if abs(lista[2][g]) > abs(maior):
            maior = lista[2][g]
        g+=1 
    return abs(maior)

lista1 = [[-1, -2, -3], [-4, -5, -6], [-10, -8, -9]]

print(encontra_maximo(lista1))