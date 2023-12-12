# Professor: 
def notas_dp(alunos):
    dps = []
    for aluno in alunos:
        if (aluno['PI'] + aluno['PF']) / 2 < 5:
            dps.append(aluno['matricula'])
    return dps



#Eu
def notas_dp(lista):
    listadp = []
    notas = 0
    for dicionario in lista:
        for val, key in dicionario.items():
            if key != 'matricula':
                notas += val
        media = val/2
        if media <5:
            listadp.append(dicionario)
    return listadp

teste = [

{'matricula' : 123, 'PI' : 7, 'PF': 3},

{'matricula' : 456, 'PI': 4, 'PF': 8},

{'matricula' : 789, 'PI': 5, 'PF': 1}

]

print(notas_dp(teste))

def notas_dp(notas):
    dp = []
    for aluno in alunos:
        if (aluno['PI'] + aluno ['PF'])/2 <5:
            dp.append(aluno['matricula'])
    return dp

teste = [

{'matricula' : 123, 'PI' : 7, 'PF': 3},

{'matricula' : 456, 'PI': 4, 'PF': 8},

{'matricula' : 789, 'PI': 5, 'PF': 1}

]

print(notas_dp(teste))

        