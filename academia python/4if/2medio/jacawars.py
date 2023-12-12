import math

velocidade = float(input("Diga a velocidade: "))
angulo = float(input("Diga o angulo: "))

angulo *=2 
g = 9.8
seno = math.sin(math.radians(angulo))

distancia = (velocidade**2 * seno)/g
print(distancia)


if distancia >=98 and distancia <=102:
    print("Acertou!")
elif distancia < 100:
    print("Muito perto")
else: 
    print("Muito longe")

