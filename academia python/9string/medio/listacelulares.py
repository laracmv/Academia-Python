def lista_celulares(lista):
    novalista = []
    for numero in lista:
        if len(numero) == 13 or len(numero) == 14:
            novaposicao = numero[5:]
            if len(novaposicao) == 9:
                novalista.append(novaposicao)
        elif len(numero) == 10 or len(numero) == 11:
            novaposicao = numero[2:]
            if len(novaposicao) == 9:
                novalista.append(novaposicao)
        else:
            novaposicao = numero
            if len(novaposicao) == 9:
                novalista.append(novaposicao)
    return novalista

print(lista_celulares(['+5511912345678', '1155556666', '77778888', '+551133334444', '918273645', '11987654321']))

