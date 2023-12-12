def soma_pecas(pecas):
    soma = 0
    for peca in pecas:
        soma +=peca[0] + peca[1]
    # peca é o primeiro elemento da lista. peca[0] é o 1 elemento dentro dessa lista 
    return soma