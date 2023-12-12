#Professor
def compras_da_semana(receitas, pratos):
    compras = {}

    for prato in pratos:
        ingredientes = receitas[prato]
        for item, qtd in ingredientes.items():
            if item not in compras:
                compras[item] = qtd
            else: 
                compras[item] +=qtd
    return compras

#Eu
def compras_da_semana(dicionario, lista):
    asercomprado = {}
    for prato in lista:
        if prato in dicionario:
            ingredientes = dicionario[prato]
            for ingrediente, quantidade in ingredientes.items():
                if ingrediente in asercomprado:
                    asercomprado[ingrediente] += quantidade
                else:
                    asercomprado[ingrediente] = quantidade

    return asercomprado

def compras_da_semana(receitas, pratos):
    novodic = {}
    for prato in pratos:
        for ingrediente, quant in receitas[prato].items():
            if ingrediente not in novodic:
                novodic[ingrediente] = quant
            else:
                novodic[ingrediente] +=quant
    return novodic

r = {
    'Bolo de chocolate': {
        'Leite': 0.25,
        'Óleo': 0.25,
        'Ovo': 2.0,
        'Farinha': 0.5,
        'Açúcar': 0.2,
        'Achocolatado': 0.3
    },
    'Bolinho de chuva': {
        'Óleo': 1.0,
        'Leite': 0.3,
        'Ovo': 3.0,
        'Farinha': 0.6,
        'Açúcar': 0.3
    },
    'Mingau': {
        'Açúcar': 0.1,
        'Maizena': 0.1,
        'Leite': 0.25
    }
}

p = ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']

print(compras_da_semana(r, p))


