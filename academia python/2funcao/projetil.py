import math

def calcula_distancia_do_projetil(v,angulo,yo):
    numerador= (v**2 *(1 + math.sqrt(1 + (2*9.8*yo)/(v**2*(math.sin(angulo)**(2))))))*math.sin(2*angulo)
    denominador= 2 * 9.8
    calulo=numerador/denominador
    return calulo