def intersecao_de_lista(l1, l2):
    l3 = []
    i = 0
    while i<len(l1):
        f = 0
        while f < len(l2):
            if l2[f] == l1[i]:
                l3.append(l2[f])
            f+=1
        i+=1
    return l3

lista1 = [2, 7, 3.1, 'banana']
lista2 = [2, 'banana', 'carro']
print(intersecao_de_lista(lista1,lista2))
