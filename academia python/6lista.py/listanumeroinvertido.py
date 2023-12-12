numero = 1
lista = []
i = 0
while numero > 0:
    numero = int(input("Digire seu valor: "))
    if numero > 0:
        lista.append(numero)
    i +=1

listainvertida = lista[::-1]
print(listainvertida)