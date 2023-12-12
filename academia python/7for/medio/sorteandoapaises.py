import random

def sorteia_pais(dicionario):
    for pais in dicionario:
        sorteado = random.choice(dicionario[pais])
    return sorteado