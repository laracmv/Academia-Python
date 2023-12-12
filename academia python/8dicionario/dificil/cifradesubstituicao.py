def decodifica(codificado, sistema):
    dinv = {}
    for k, v in sistema.items():
        saida[v] = k
    original = ''
    for l in codificada:
        if  l in dinv:
            original +=dinv[l]
        else:
            original +=l
    return original

pr