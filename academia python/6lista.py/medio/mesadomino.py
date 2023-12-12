def adiciona_na_mesa(peca, mesa):
    i = 0
    saida = mesa
    if mesa == []:
        return [peca]
    else:
        while i<len(mesa):
            if i == 0 or i == len(mesa) -1:
                if peca[1] == mesa[i][0]:
                    saida.insert(0, peca)
                    return saida
                elif peca[0] == mesa[i][0]:
                    invertido = peca[::-1]
                    # inverte a lista 
                    saida.insert(0, invertido)
                    return saida
                elif peca[0] == mesa[i][-1]:
                    # o -1 pega o ultimo elemento da lista
                    saida.append(peca)
                    return saida
                elif peca[1] == mesa[i][-1]:
                    invertido = peca[::-1]
                    saida.append(invertido)
                    return saida
            i+=1
        return saida

p = [2,6]
m = [[3,1],[1,6],[6,6],[6,2]]
print(adiciona_na_mesa(p,m))
