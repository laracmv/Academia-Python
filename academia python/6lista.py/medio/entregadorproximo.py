import math

def distancia(x1,x2,y1,y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def entregador_mais_proximo(rest, entreg):
    i = 0
    indice = 0
    prox = distancia(rest[0],entreg[0][0],rest[1], entreg[0][1])
    while i < len(entreg):
        if distancia(rest[0],entreg[i][0],rest[1], entreg[i][1] ) < prox:
            indice = i
        i+=1
    return indice

print(entregador_mais_proximo([3,4], [[10, 20],[4, 2],[100, 74],[23, 63]]))