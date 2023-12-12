def tem_estoque(pecasconstrucao, pecasestoque):
    retorno = None
    for keyconst, valueconst in pecasconstrucao.items():
        if keyconst not in pecasestoque: 
            return False
        else:
            for keyestoque, valueestoque in pecasestoque.items():
                if keyconst == keyestoque:
                    if valueestoque >= valueconst :
                        retorno = True
                    else: 
                        return False
    return retorno

def tem_estoque(pecas, estoque):
    for item, quant in pecas.items():
        if item not in estoque:
            return False
        else:
            quantestoque = estoque[item]
            if quantestoque <  quant :
                return False
    return True


constr = {
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3,
}
estoque = {
    'hélice': 149,
    'motor': 56,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 1304,
    'turbina': 23,
}

print(tem_estoque(constr, estoque))
