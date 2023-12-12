from math import sqrt

def calcula_tempo(dic):
    dicionario = {}
    for nome in dic:
        resp = sqrt(100*2/dic[nome])
        dicionario[nome] = resp
    return dicionario
        
