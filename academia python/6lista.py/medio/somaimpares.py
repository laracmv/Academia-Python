def soma_impares(lista):
    i = 0
    soma = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            soma += lista[i]
        i +=1
    return soma

l1 = [1,2,3,4]
print(soma_impares(l1))