import math

def distancia_euclidiana(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

# Exemplo de uso da função
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

resultado = distancia_euclidiana(x1, y1, x2, y2)
print("A distância entre os pontos é:", resultado)