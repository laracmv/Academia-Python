def conta_ocorrencias(lista):
    dicionario = {}
    for elementos in lista:
        if elementos not in dicionario:
            dicionario[elementos] =1
        else:
            dicionario[elementos] += 1
    return dicionario

lis = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']

print(conta_ocorrencias(lis))