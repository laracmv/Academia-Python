def calcula_overbooking(capacidade, listapassagens):
    excesso = 0
    if listapassagens == []:
        return 0
    else:
        i = 0
        while i < len(listapassagens):
            if listapassagens[i]>capacidade:
                excesso += listapassagens[i] - capacidade
            i+=1
        return excesso
