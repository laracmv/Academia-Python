# Faça uma função que receba uma matriz (listas dentro de lista) e retorna uma lista com os valores mínimos de cada coluna (na mesma ordem das colunas).

# Por exemplo:

# Entrada:

# minimos_colunas([
#     [2, 4, -1, 3],
#     [0, 7, 6, 4],
#     [8, 1, 2, 3]
# ])
# Saída:

# [0, 1, -1, 3]

def minimos_colunas(x):
    min1 = 10
    min2 = 10
    min3 = 10
    min4 = 10
    min=[]
    linha=0 
    while linha<len(x):
        col = 0
        while col < len(x):
            if x[linha][0] < min1:
                min1 = x[linha][0]
            if x[linha][1] < min2:
                min2 = x[linha][1]
            if x[linha][2] < min3:
                min3 = x[linha][2] 
            if x[linha][3] < min4:
                min4 = x[linha][3]   
            linha+=1
            col +=1
        min.append(min1)
        min.append(min2)
        min.append(min3)
        min.append(min4)
    return min

minimos_col = ([
    [2, 4, -1, 3],
    [0, 7, 6, 4],
    [8, 1, 2, 3]
])

print(minimos_colunas(minimos_col))