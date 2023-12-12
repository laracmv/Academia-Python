def promocao_viagens(dicionario):
    dicionario2 = {}
    for viagem, itens in dicionario.items():
        if itens[0] == 1:
            valor = 0.9 * itens[1]
            dicionario2[viagem] = valor
        elif itens[0] == 2:
            valor = 0.8 * itens[1]
            dicionario2[viagem] = valor
        elif itens[0] == 3:
            valor = 0.7 * itens[1]
            dicionario2[viagem] = valor
        elif itens[0] == 4:
            valor = 0.6 * itens[1]
            dicionario2[viagem] = valor
        elif itens[0] == 5:
            valor = 0.5 * itens[1]
            dicionario2[viagem] = valor
    return dicionario2
        
            
def promocao_viagens(d):
    dic = {}
    for destino, lista in d.items():
        if lista[0] ==1:
            novopreco = lista[1] * 0.9
        elif lista[0] ==2:
            novopreco = lista[1] * 0.8
        elif lista[0] ==3:
            novopreco = lista[1] * 0.7
        elif lista[0] ==4:
            novopreco = lista[1] * 0.6
        else:
            novopreco = lista[1] * 0.5
        dic[destino] = novopreco
    return dic
de = {
    "Miami" : [1, 1000],
    "Ilhas Sandwich do Sul" : [4, 5000],
    "Barcelona" : [2, 2000],
    "Antártica" : [5, 200],
    "Buenos Aires" : [3, 500]
}

print(promocao_viagens(de))