matriz = [
    [5,6,7],
     [8,9,10]
     ]
soma = 0

for linha in matriz:
    for elemento in linha:
        soma += elemento
print(soma)