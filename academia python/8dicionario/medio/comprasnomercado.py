def valor_a_devolver(prateleira, caixa, compras):
    retorno = 0
    for compra in compras:
        produto = compra[0]
        marca = compra[1]
        qtd = compra[2]
        vprat = prateleira[produto][marca]
        vcaixa = caixa[produto][marca]
        if vcaixa > vprat:
            retorno += (vcaixa - vprat) * qtd
    return retorno

#Refeito
def valor_a_devolver(prateleira, caixa, compras):
    retorno = 0
    for prodlista in compras:
        prod = prodlista[0]
        marca = prodlista[1]
        quant = prodlista[2]
        valprat = prateleira[prod][marca]
        valcaixa = caixa[prod][marca]
        if valprat != valcaixa:
            if valcaixa - valprat > 0:
                retorno += (valcaixa - valprat) * quant
    return retorno


p = {
    'requeijão': {
        'Minas': 5,
        'Buritis': 6,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10,
        'Lavagem Perfeita': 12.5,
        'Cromo': 15.7
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 25
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4,
        'Urbano': 5.3
    }
}

c = {
    'requeijão': {
        'Minas': 10,
        'Buritis': 7,
        'Queijinho': 7 
    },
    'sabão': {
        'Pura Espuma': 10.5,
        'Lavagem Perfeita': 12.8,
        'Cromo': 15.8
    },
    'arroz': {
        'Prato Fundo': 20,
        'Tio José': 23,
        'Cadez': 23
    },
    'macarrão': {
        'Sandra': 2,
        'Massa Nobre': 4.5,
        'Urbano': 5.3
    }
}

comp = [
    ['arroz','Cadez',2],
    ['requeijão','Minas',3],
    ['requeijão','Queijinho',1],
    ['sabão','Cromo',2]
]

print(valor_a_devolver(p,c ,comp))