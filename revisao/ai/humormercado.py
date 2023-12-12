# Detecção de comportamento do mercado financeiro é uma tarefa de grande valia para projeções econômicas. Faça uma função em Python que receba uma lista com operações de um ativo dia-a-dia, onde cada item da lista é uma lista de operações ao longo de um dia. Sua função deve retornar uma lista com a operação mais frequente por dia.

# Exemplo:

# entrada:

# [
#     ['vender', 'comprar', 'vender'],
#     ['comprar', 'comprar', 'vender'],
#     ['comprar', 'vender' ],
#     ['vender', 'comprar', 'vender', 'vender']
# ]
# retorno:

# [
#     'vender',
#     'comprar',
#     'empate',
#     'vender'
# ]
# Note: no caso de empate, mesma quantidade de vender e comprar, então, o dia deve registrar empate.

def mercado(lista):
    novalista = []
    for i in range(len(lista)):
        comprar = 0
        vender = 0 
        for f in range(len(lista[i])):
            if lista[i][f] == 'comprar':
                comprar +=1
            else:
                vender +=1

        if comprar == vender:
            novalista.append('empate')
        elif comprar > vender:
            novalista.append('comprar')
        else:
            novalista.append('vender')
    return novalista

l = [
    ['vender', 'comprar', 'vender'],
    ['comprar', 'comprar', 'vender'],
    ['comprar', 'vender' ],
    ['vender', 'comprar', 'vender', 'vender']
]

print(mercado(l))

