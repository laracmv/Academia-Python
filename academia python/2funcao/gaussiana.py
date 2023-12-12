import math

def calcula_gaussiana(x, mi, sigma):
    numerador = math.e ** (-((x - mi) ** 2) / (2 * sigma ** 2))
    denominador = sigma * math.sqrt(2 * math.pi)
    calculo = numerador / denominador
    return calculo