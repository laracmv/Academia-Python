import math

def encontra_uma_raiz(a,b,c):
    delta= b**2 - 4*a*c
    raiz= (-b+(delta)**(1/2))/(2*a)
    return raiz

a=2
b=0
c= -200

resultado=encontra_uma_raiz(a,b,c)
print(resultado)