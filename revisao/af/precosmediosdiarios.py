def preco_medio(lista):
    i = 0
    novodic = {}
    contador = {}
    while i< len(lista):
        ativo = lista[i][0]
        valor = lista[i][2]
        
        if ativo not in novodic:
            novodic[ativo] = valor
            contador[ativo] = 1
        else:
            novodic[ativo] += valor
            contador[ativo] +=1
        i +=1 
    
    for ativo2 in novodic:
        novodic[ativo2] = novodic[ativo2] / contador[ativo2]
    
    return novodic

l = [
	['BBAS3', '11:09:05', 51.32],
	['USIM5', '15:25:42', 16.77],
	['USIM5', '16:00:08', 11.84],
	['BBAS3', '16:12:46', 55.59],
	['SLCE3', '16:13:39', 37.74]
]

print(preco_medio(l))