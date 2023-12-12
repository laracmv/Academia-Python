def calcula_porcentagens(dicionario):
    soma = 0
    dicionario2 = {}
    for valores in dicionario.values():
        soma += valores
    for key, valores in dicionario.items():
        porcentagem = (valores/soma)* 100
        dicionario2[key] = porcentagem
    return dicionario2

v = {
    'Erro de indentação': 493,
    'Erro de parênteses': 1102,
    'Variável inexistente': 405,
}

print(calcula_porcentagens(v))

