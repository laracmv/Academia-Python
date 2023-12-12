def distancia(x1,y1,x2,y2,p):
    parte1=abs((x1-x2)**p)
    parte2=abs((y1-y2)**p)
    d= (parte1+parte2)**(1/p)
    return d