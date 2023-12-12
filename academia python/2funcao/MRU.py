def calcula_posicao(t, so,v):
    s=so+v*t
    return s

so=10
v=2
t=2
posicao=calcula_posicao(t,so,v)
print(posicao)