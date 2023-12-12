import math

def hellinger(media1,desv1,media2,desv2):
    expocima= -1*(media1-media2)**2
    basexp= 4*(desv1**2+desv2**2)
    expoente= expocima/basexp
    partecimaraiz= 2*desv1*desv2
    partebaixoraiz= desv1**2+desv2**2
    raiz= math.sqrt(partecimaraiz/partebaixoraiz)
    d= 1 - raiz *math.e ** expoente
    return d