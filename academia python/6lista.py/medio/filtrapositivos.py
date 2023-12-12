# Faça uma função que recebe uma lista de números reais e retorna uma nova lista contendo apenas os números estritamente positivos da lista original.

# O nome da sua função deve ser filtra_positivos

def filtra_positivos(lista):
    i=0
    lista2 = []
    while i<len(lista):
        if lista[i] > 0:
            lista2.append(lista[i])
        i+=1
    return lista2