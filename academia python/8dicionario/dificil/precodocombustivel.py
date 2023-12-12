def contabiliza_combustivel(dic):
    dicnovo = {}

    for dia, dados in dic.items():
        tipo = dados['tipo']
        litros = dados['litros']
        custo  = dados['custo']
        
        if tipo not in dicnovo:
            dicnovo[tipo] = {}
            dicnovo[tipo]['total litros'] = litros
            dicnovo[tipo]['custo por litro'] = custo
            
        else:
            dicnovo[tipo]['total litros'] +=litros
            dicnovo[tipo]['custo por litro'] += custo
    
    for tiponovo, dadosnovos in dicnovo.items():
        total = dadosnovos['total litros']
        clitro = dadosnovos['custo por litro']

        dicnovo[tiponovo]['custo por litro'] = clitro/total

    return dicnovo

e = {
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}

print(contabiliza_combustivel(e))