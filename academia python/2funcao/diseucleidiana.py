

def distancia_euclidiana(x1,y1,x2,y2):
    distancia=((x2-x1)**2 + (y2-y1)**2) **(1/2)
    return distancia 

x1=1
y1=4
x2=3
y2=8

distancia= distancia_euclidiana(x1,y1,x2,y2)
print(distancia)