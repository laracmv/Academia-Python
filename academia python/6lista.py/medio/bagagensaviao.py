def filtra_bagagens(listabagagem, limitealtura, limitelargura, limiteprofundidade):
    excesso = 0
    listaexcesso = []
    i = 0
    while i < len(listabagagem):
        if listabagagem[i][0] > limitealtura or listabagagem[i][1] > limitelargura or listabagagem[i][2] > limiteprofundidade:
            excesso +=1
            listaexcesso.append(listabagagem[i][0])
            listaexcesso.append(listabagagem[i][1])
            listaexcesso.append(listabagagem[i][2])
        i+=1
    return excesso

print(filtra_bagagens([[43.2, 30.5, 20.1], [60.0, 20.0, 20.0], [10.0, 10.0, 10.0], [50.3, 30.2, 30.0], [54.0, 30.2, 22.1]], 55, 35, 25))    




