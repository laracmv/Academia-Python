# def pais_campeao(medalhas):
#     maiorouro = None
#     maiorprata = None
#     maiorbronze = None
#     pouro = None
#     pprata = None
#     pbronze = None
#     douro = []
#     dprata = []
#     dbronze = []
#     for pais in medalhas.keys():
#         quantouro = medalhas[pais]['ouro']
#         douro.append(quantouro)
        
#         prata = medalhas[pais]['prata']
#         dprata.append(prata)
#         bronze = medalhas[pais]['bronze']
#         dbronze.append(dbronze)
        
#         if maiorouro == None or quantouroouro > maiorouro:
#             maiorouro = quantouro
#             pouro = pais
#     return 

# def pais_campeao(medalhas):
#     maior = None
#     for pais in medalhas.keys():
#         qouro = medalhas[pais]['ouro']
        

#         if maior == qouro:
#             maior = None
#             for pais in medalhas.keys():
#                 qprata = medalhas[pais]['prata']
#                 if maior == qprata:
#                     maior = None
#                     for pais in medalhas.keys():
#                         qbronze = medalhas[pais]['bronze']
#                         if maior == None or qbronze > maior:
#                             maior = qbronze
#                             p = pais
#                 if maior == None or qprata > maior:
#                     maior = qprata
#                     p = pais
#         if maior == None or qouro > maior:
#             maior = qouro
#             p = pais
#     return p

def pais_campeao(quadro):
    # verifica ouros
    vencedores_ouro = []
    max_ouro = 0
    for pais, medalhas in quadro.items():
        if medalhas['ouro'] == max_ouro:
            vencedores_ouro.append(pais)
        if medalhas['ouro'] > max_ouro:
            vencedores_ouro = [pais]
            max_ouro = medalhas['ouro']

    if len(vencedores_ouro) == 1:
        return vencedores_ouro[0]

    # verifica pratas
    vencedores_prata = []
    max_prata = 0
    for pais in vencedores_ouro:
        qtd_prata = quadro[pais]['prata']
        if qtd_prata == max_prata:
            vencedores_prata.append(pais)
        if qtd_prata > max_prata:
            vencedores_prata = [pais]
            max_prata = qtd_prata

    if len(vencedores_prata) == 1:
        return vencedores_prata[0]

    # verifica bronzes
    vencedores_bronze = []
    max_bronze = 0
    for pais in vencedores_prata:
        qtd_bronze = quadro[pais]['bronze']
        if qtd_bronze == max_bronze:
            vencedores_bronze.append(pais)
        if qtd_bronze > max_bronze:
            vencedores_bronze = [pais]
            max_bronze = qtd_bronze

    return vencedores_bronze[0]

p = {
    'Noruega': {
        'ouro': 1,
        'prata': 1,
        'bronze': 2 
    },
    'Egito': {
        'ouro': 0,
        'prata': 4,
        'bronze': 1
    },
    'Áustria': {
        'ouro': 0,
        'prata': 4,
        'bronze': 0
    },
    'Tunísia': {
        'ouro': 1,
        'prata': 0,
        'bronze': 3
    }
}

print(pais_campeao(p))

