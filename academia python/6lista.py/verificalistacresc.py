def eh_crescente(lista):
    i=0
    cresc = None
    while i<len(lista):
        if lista[i] + lista[i+1] > 0:
            cresc = True
        else: 
            cresc = False
        i+=1
    if cresc == False:
        return False
    else:
        return True
    
lista1 = [1,2,3,4]
print(eh_crescente(lista1))