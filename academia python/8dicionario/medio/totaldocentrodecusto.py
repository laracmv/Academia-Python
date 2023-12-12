def total_centro_custo(dicionario):
    dicionario2 = {}

    for nomes in dicionario:
        setor = dicionario[nomes]["centro de custo"]
        if setor not in dicionario2:
            dicionario2[setor] = dicionario[nomes]["valor"]
        else:
                dicionario2[setor] += dicionario[nomes]["valor"]
    return dicionario2


entrada = {
    'Joao Silva': {
        'descricao': 'passagem para auditoria em filial',
        'centro de custo': 'tesouraria',
        'valor': 3000,
    },
    'Silvio Costa': {
        'descricao': 'alimentacao em processo de auditoria',
        'centro de custo': 'tesouraria',
        'valor': 1340.50,
    },
    'Maria Conceicao': {
        'descricao': 'inscricao em congresso internacional',
        'centro de custo': 'presidencia',
        'valor': 7200.00,
    },
    'Marcio Macedo': {
        'descricao': 'copias de memorando',
        'centro de custo': 'producao',
        'valor': 30.80,
    },
    'Marisa Monte Verde': {
        'descricao': 'curso em complaince',
        'centro de custo': 'presidencia',
        'valor': 17800.00,
    }
}

print(total_centro_custo(entrada))

