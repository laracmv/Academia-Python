def posicoes_possiveis(mesa, lista):
    posicoes = []
    if mesa == []:
        for pecas in lista:
            for elementos in pecas:
                posicoes.append(lista.index(pecas)) 
                break
    else:
        for pecas in lista:
            for elemento in pecas:
                
                if elemento == mesa[0][0] and elemento == mesa[-1][1]:
                    posicoes.append(lista.index(pecas))
                elif elemento == mesa[0][0] or elemento == mesa[-1][1]:
                    posicoes.append(lista.index(pecas))
                    break

    return posicoes


mesa = [[0,2],[2,1],[1,6],[6,5],[5,3]]

p = [[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6]]

print(posicoes_possiveis(mesa, p))
                

