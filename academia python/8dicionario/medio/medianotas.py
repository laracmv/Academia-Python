def notas_dp(lista):
    listadp = []
    notas = 0
    for dicionario in lista:
        for key, val in dicionario.items():
            if key == 'matricula':
                listadp.append(val)
            if key != 'matricula':
                notas += val
            if key == 'PF':
                media = notas/2
                if media >= 5:
                   listadp.pop()
                notas = 0
    return listadp

teste = [

{'matricula' : 123, 'PI' : 7, 'PF': 3},

{'matricula' : 456, 'PI': 4, 'PF': 8},

{'matricula' : 789, 'PI': 5, 'PF': 1}

]

print(notas_dp(teste))