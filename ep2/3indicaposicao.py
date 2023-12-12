# Para o jogo Termo, é importante saber quais letras de uma palavra especulada correspondem a uma posição acertada ou não na palavra sorteada, para isso, faça uma função que recebe a palavra sorteada e a palavra especulada, retornando uma lista onde:

# 0 se a letra da palavra especulada está na posição correta da palavra sorteada;
# 1 se a letra da palavra especulada existe na palavra sorteada, e;
# 2 se a letra da palavra especulada não existe na palavra sorteada.

# Exemplo 1:
# entradas:

# sorteada = 'escolhe'
# especulada = 'sacolas'

# retorno:
# [1, 2, 0, 0, 0, 2, 1]

# Exemplo 2:
# entradas:

# sorteada = 'escolhe'
# especulada = 'escola'
# retorno:
# []

# Retorne [] caso o tamanho das palavras diverjam.

# O nome da sua função deve ser inidica_posicao

def inidica_posicao(sorteada, especulada):
    posicao = []
    if len(sorteada) != len(especulada):
        return posicao
    else:
        i = 0
        while i < len(sorteada):
            if sorteada[i] == especulada[i]:
                posicao.append(0)
            elif sorteada[i] == especulada[f]:
                posicao.append(1)
            else:
                posicao.append(2)
            i+=1
        return posicao

sort = 'escolhe'
espec = 'sacolas'

print(inidica_posicao(sort, espec))
