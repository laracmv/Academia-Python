from math import sqrt

def calcula_tempo(d):
    dicionario = {}
    for nome in d:
        resp = sqrt(100*2/d[nome])
        dicionario[nome] = resp
    return dicionario
        

nome = None
aceleracao = None
minimo = None
nomeminimo = None
dicionario = {}
while nome != "sair" :
    nome = input("Diga o seu nome")
    if nome == "sair":
        break
    aceleracao = float(input("Diga sua aceleracao: "))
    tempo = sqrt(100*2/aceleracao)
    dicionario[nome] = aceleracao
    continue
dictempo = calcula_tempo(dicionario)
    

for key, val in dictempo.items():
    if minimo is None or val < minimo:
        nomeminimo = key
        minimo = val


print(f"{nomeminimo} é o nome do vencedor e {minimo} é o seu tempo de conclusão")
