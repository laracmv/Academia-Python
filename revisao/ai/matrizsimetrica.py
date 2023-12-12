# Verificar se uma matriz é simétrica é vital para determinadas operações de sistemas multidimensionais. Uma matriz simétrica é quadrada e a diagonal principal separa o canto superior direito do canto inferior esquerdo, onde os cantos são "espelhos" um do outro. Exemplo:

# [
#     [1, 2, 3, 4],
#     [2, 5, 7, 8],
#     [3, 7, 7, 0],
#     [4, 8, 0, 8]
# ]
# Faça uma função que receba uma matriz e retorne True se for simétrica ou False se não for simétrica.

def matrizsimetrica(matriz):
    i = 1
    while i < len(matriz):
        if len(matriz[i]) != len(matriz):
            return False
        j = 0
        while j < len(matriz):
            v1 = matriz[i][j]
            v2 = matriz[j][i]
            if v1 != v2:
                return False
            j+=1
        i+=1
            
    return True

m = [
    [1, 2, 3, 4],
    [2, 5, 7,5],
    [3, 7, 7,0],
    [4, 8, 0, 8]
]

print(matrizsimetrica(m))