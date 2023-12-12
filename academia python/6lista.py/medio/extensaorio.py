from math import *

def calcula_extensao(x,y):
    i = 0
    distancia = 0 
    while i < len(x) - 1:
        distancia += sqrt((x[i+1]-x[i])**2 + (y[i+1] - y[i])**2)
        i+=1
    return distancia

xt = [275, 290, 310, 390, 480]
yt = [75, 180, 120, 110, 150]

print(calcula_extensao(xt,yt))