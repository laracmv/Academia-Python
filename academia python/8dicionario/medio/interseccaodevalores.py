def interseccao_valores(d1, d2):
    lista = []
    for value1 in d1.values():
        for value2 in d2.values():
            if value1 == value2:
                lista.append(value1)
    return lista