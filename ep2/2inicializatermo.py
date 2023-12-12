# Trabalhar com dicionário é extremamente útil para manipular a configuração de um ambiente por exemplo. No jogo Termo, é interessante, ao iniciar o jogo, criar um dicionário com a configuração do jogo a fim de manter os dados coesos em apenas um ponto do código.

# Faça uma função que receba uma lista de palavras, todas de mesmo tamanho, e devolva um dicionário onde:

# n: é o número de letras das palavras;
# tentativas: é o número máximo da tentativas, iniciado com n+1;
# especuladas: lista de palavras já especuladas pelo jogador, iniciar com [];
# sorteada: a palavra sorteada, dentra as palavras da lista de entrada, pelo computador. Utilize obrigatoriamente a função choice da bibliioteca random.
# Exemplo:

# entrada:

# palavras = [
#     'uivo', 'vimo', 'rife',
#     'abas', 'clas', 'mujo',
#     'pata', 'seta', 'veja'
# ]
# retorno:

# {
#     'n': 4,
#     'sorteada': 'uivo',
#     'especuladas': [],
#     'tentativas': 5
# }
# O nome da sua função deve ser inicializa

import random

def inicializa(listadepalavras):
    dicionario = {}
    dicionario["n"] = len(listadepalavras[0])
    dicionario["sorteada"] = random.choice(listadepalavras)
    dicionario["especuladas"] = []
    dicionario["tentativas"] = dicionario["n"] + 1
    return dicionario

palavras = [
    'uivo', 'vimo', 'rife',
    'abas', 'clas', 'mujo',
    'pata', 'seta', 'veja'
]

print(inicializa(palavras))