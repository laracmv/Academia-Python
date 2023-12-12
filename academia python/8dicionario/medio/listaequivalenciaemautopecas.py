def melhor_valor(compras, inventario):
    total = 0
    for prod in compras:
        valor = 0
        for possivel in inventario:
            if possivel["serial"] == prod:
                valor = possivel["valor"]
        for possivel in inventario:
            if prod in possivel["equivalente"]:
                if valor == 0 or possivel["valor"] < valor:
                    valor = possivel["valor"]
        total +=valor
    return total




def melhor_valor(lpecas, lestoque):
    final = 0
    for peca in lpecas:
        menorvalor = 0
        iniciomenorvalor = 0
        i = 0
        while i < len(lestoque):
            if peca in lestoque[i]['serial'] or peca in lestoque[i]['equivalente']:
                valor = lestoque[i]['valor']
                if iniciomenorvalor == 0:
                    menorvalor = valor
                    iniciomenorvalor +=1
                else:
                    if valor < menorvalor:
                        menorvalor = valor
            i+=1
        final += menorvalor
    return final

partes = ['X1D', 'A3B']

inventario = [
    {'serial': 'A3B', 'valor': 198.7, 'equivalente': []},
    {'serial': 'XP2', 'valor': 190.9, 'equivalente': ['Z3Z', 'A3B']},
    {'serial': 'XP1', 'valor':   5.1, 'equivalente': ['TH5', 'TH6', 'X3D', 'X1D']}
]

print(melhor_valor(partes, inventario))

        



