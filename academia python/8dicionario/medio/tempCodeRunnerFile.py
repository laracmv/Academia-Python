def tem_estoque(pecas, estoque):
    for item, quant in pecas.items():
        if item not in estoque:
            return False
        else:
            qestoque = estoque[item]
            if quant >= estoque[item]:
                return True
            else:
                return False


constr = {
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3
}

estoque = {
    'hélice': 149,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 20,
    'turbina': 23
}

print(tem_estoque(constr, estoque))

def tem_estoque(dpecas, destoque):
    for peca, quant in dpecas.items():
        if peca not in destoque:
            return False
        if destoque[peca] < dpecas[peca]:
            return False
    return True

p = {
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3,
}

e = {
    'hélice': 149,
    'motor': 56,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 1304,
    'turbina': 23,
}

print(tem_estoque(p,e))

