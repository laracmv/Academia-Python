def inverte_dicionario(dic):
    novodic = {}
    for nome, idade in dic.items():
        if idade not in novodic:
            novodic[idade] = [nome]
        else:
            novodic[idade].append(nome)
    return novodic

d = {'Ana': 19, 'Bruno': 18, 'João': 19}
print(inverte_dicionario(d))
