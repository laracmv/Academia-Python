def monitora_represas(inicial, variacao):
    total = {}
    cap = {}
    novodic = {}

    for represa, dados in inicial.items():
        capacidade = dados['capacidade']
        cap[represa] = capacidade
        volume = dados['volume']
        total[represa] = (capacidade * 100)/volume
        

    for varrepresa, vardados in variacao.items():
        for dia, valores in vardados.items():
            
            entra = valores[0]
            sai = valores[1]
            variacao  = entra - sai
            if variacao > 0:
                cap[varrepresa] += variacao
            else:
                cap[varrepresa] -= abs(variacao)
        
        porcentagem = (cap[varrepresa]/total[varrepresa]) * 100
        
        if porcentagem >= 0 and porcentagem <20:
            if 'emergencia' not in novodic:
                novodic['emergencia'] = [varrepresa]
            else:
                novodic['emergencia'].append(varrepresa)
        elif porcentagem >= 20 and porcentagem < 50:
            if 'critico' not in novodic:
                novodic['critico'] = [varrepresa]
            else:
                novodic['critico'].append(varrepresa)
        elif porcentagem >= 50 and porcentagem < 70:
            if 'atencao' not in novodic:
                novodic['atencao'] = [varrepresa]
            else:
                novodic['atencao'].append(varrepresa)
        elif porcentagem >=70 and porcentagem <100:
            if 'normal' not in novodic:
                novodic['normal'] = [varrepresa]
            else:
                novodic['normal'].append(varrepresa)
        else:
            if 'escoar' not in novodic:
                novodic['escoar'] = [varrepresa]
            else:
                novodic['escoar'].append(varrepresa)
        
            
    return novodic

# estado_inicial = {
#     'cantareira': {
#         'capacidade': 982000,
#         'volume': 25
#     },
#     'guarapiranga': {
#         'capacidade': 171000,
#         'volume': 95
#     },
#     'alto tiete': {
#         'capacidade': 540000,
#         'volume': 55
#     }
# }

# variacoes = {
#     'cantareira': {
#         '01': [5000,30000],
#         '02': [10000,35000],
#         '03': [0,29000],
#         '04': [31000,28000],
#         '05': [0,29000]
#     },
#     'guarapiranga': {
#         '01': [6000,10000],
#         '02': [38000,12000],
#         '03': [35000,14000],
#         '04': [0,13000],
#         '05': [15000,12000]
#     },
#     'alto tiete': {
#         '01': [18000,30000],
#         '02': [15000,25000],
#         '03': [17700,24000],
#         '04': [41000,28000],
#         '05': [13000,24000]
#     }

# }

# print(monitora_represas(estado_inicial, variacoes))
        
def monitora_represas(estado_inicial, variacoes):
    classificacao = {'emergencia': [], 'critico': [], 'atencao': [], 'normal': [], 'escoar': []}

    for represa, dados_iniciais in estado_inicial.items():
        capacidade = dados_iniciais['capacidade']
        volume = dados_iniciais['volume']

        for dia, variacao in variacoes[represa].items():
            precipitacao, demanda = variacao
            volume += precipitacao - demanda

        # Verifica a classificação com base no volume em %
        percentual = (volume / capacidade) * 100

        if percentual < 20:
            classificacao['emergencia'].append(represa)
        elif percentual < 50:
            classificacao['critico'].append(represa)
        elif percentual < 70:
            classificacao['atencao'].append(represa)
        elif percentual <= 100:
            classificacao['normal'].append(represa)
        else:
            classificacao['escoar'].append(represa)

    # Remove pontuação nas chaves
    classificacao_sem_pontuacao = {key.replace('-', ''): value for key, value in classificacao.items()}

    return classificacao_sem_pontuacao

# Exemplo de chamada
estado_inicial = {
    'cantareira': {'capacidade': 982000, 'volume': 25},
    'guarapiranga': {'capacidade': 171000, 'volume': 95},
    'alto tiete': {'capacidade': 540000, 'volume': 55}
}

variacoes = {
    'cantareira': {'01': [5000, 30000], '02': [10000, 35000], '03': [0, 29000], '04': [31000, 28000], '05': [0, 29000]},
    'guarapiranga': {'01': [6000, 10000], '02': [38000, 12000], '03': [35000, 14000], '04': [0, 13000], '05': [15000, 12000]},
    'alto tiete': {'01': [18000, 30000], '02': [15000, 25000], '03': [17700, 24000], '04': [41000, 28000], '05': [13000, 24000]}
}

resultado = monitora_represas(estado_inicial, variacoes)
print(resultado)
