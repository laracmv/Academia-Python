import math

i = 0
while i<91:
    senbaskara = (4 * i * (180 - x))/(40500 - x * (180 - x))
    seno = math.sin(radians(i))
    diferenca = abs(senbaskara - seno)
    if i == 0:
        maior = diferenca   
    else: 
        