# Calculo de um Movimento Retilineo Uniformemente Variado

def calcula_posicao(posicaoinicial,velocidadeinicial,aceleracao,tempo):
    posicao=posicaoinicial+velocidadeinicial*tempo+(aceleracao*tempo**2)/2
    return posicao
