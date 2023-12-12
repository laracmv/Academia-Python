def verifica_lista(lista1):
    i=0
    par = 0
    impar = 0
    if len(lista1) == 0:
        return "misturado"
    while i<len(lista1):
        if lista1[i] % 2 == 0:
            par +=1
        if lista1[i] % 2 == 1 or lista1[i] ==1:
            impar +=1
        i+=1
    if par == len(lista1):
        return "par" 
    if impar == len(lista1):
        return "ímpar"
    return "misturado"


lista = [3,5]

print(verifica_lista(lista))
        