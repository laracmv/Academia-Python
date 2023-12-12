def bagagens(lfranquias, ldespachado):
    lorganizada = []
    retorno = []
    i = 0
    while i < len(franquias):
        for f in range(len(ldespachado)):
            if ldespachado[f][0] == i:
                lorganizada.append(ldespachado[f])
        i+=1

    for g in range(len(lorganizada)):
        pagar = 0
        mala = 1
        nmalas = 0
        while mala < len(lorganizada[g]):
            if lorganizada[g][mala] > lfranquias[g][1] :
                passou = abs(lfranquias[g][1] - lorganizada[g][mala])
                pagar += passou * 50
            nmalas +=1
            mala +=1

        if nmalas > lfranquias[g][0]:
            pagar += 300
        retorno.append(pagar)


    return lorganizada

franquias = [ [1, 10], [0, 23], [2, 32] ]
despachadas = [ [1, 22], [2, 31, 32] ]

print(bagagens(franquias, despachadas))


#----Chatgpt
def bagagens(lfranquias, ldespachado):
    retorno = []

    for i in range(len(lfranquias)):
        pagar = 0
        nmalas = 0

        for entry in ldespachado:
            if entry[0] == i:
                for mala in entry[1:]:
                    if mala > lfranquias[i][1]:
                        passou = abs(lfranquias[i][1] - mala)
                        pagar += passou * 50
                nmalas += 1

        if nmalas > lfranquias[i][0]:
            pagar += 300
        retorno.append(pagar)

    return retorno

franquias = [[1, 10], [0, 23], [2, 32]]
despachadas = [[1, 22], [2, 31, 32]]

print(bagagens(franquias, despachadas))

