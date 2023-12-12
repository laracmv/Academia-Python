def classifica_trigo(lista):
    saida = []
    if lista == []:
        return []
    else: 
        for i in lista:
            if i <=2: 
                saida.append("T1")
            elif i <=3:
                saida.append("T2")
            elif i <=7:
                saida.append("T3")
            else:
                saida.append("FT")
    return saida

