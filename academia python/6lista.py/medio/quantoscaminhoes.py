def quantos_caminhoes(lista):
    i = 0
    soma = 0
    caminhao = 0
    while i < len(lista):
        if lista[i] < 2000:
            soma += lista[i]
        if soma >=2000:
            soma = abs(soma-2000)
            caminhao+=1
        i+=1
    if soma > 0:
        caminhao +=1
    return caminhao
    

cam = [1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]

print(quantos_caminhoes(cam))