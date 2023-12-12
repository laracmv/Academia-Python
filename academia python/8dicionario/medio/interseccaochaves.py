def interseccao_chaves(d1, d2):
    lista = []
    for key1 in d1.keys():
        for key2 in d2.keys():
            if key1 == key2:
                lista.append(key1)
    return lista

c = {"d":1, "c": 2}
d = {"k":0, "d": 1, "c":3}

print(interseccao_chaves(c,d))
