def verifica_ganhador(dic):
    for jogador, pecas in dic.items():
        if pecas == []:
            return jogador
    return -1

entrada = {
    0: [[1,1],[1,2],[0,0],[1,4],[1,5]],
    1: [],
    2: [[3,6],[2,4],[3,4],[2,3]],
    3: [[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]]
}

print(verifica_ganhador(entrada))
