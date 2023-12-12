def raiz_quadrada(n):
    primo=1
    raiz=1
    while primo != n:
        n-= primo
        primo+=2
        raiz+=1
    return raiz

numero = 4
print(raiz_quadrada(numero))