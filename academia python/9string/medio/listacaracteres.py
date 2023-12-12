def lista_caracteres(string):
    lista = []
    for palavra in string:
        if palavra not in lista:
            lista.append(palavra)
    return lista
