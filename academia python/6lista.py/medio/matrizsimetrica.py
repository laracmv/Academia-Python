def simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False

    n = len(matriz)
    linhas = 0

    while linhas < n:
        colunas = 0
        while colunas < linhas:
            if matriz[linhas][colunas] != matriz[colunas][linhas]:
                return False
            colunas += 1
        linhas += 1

    return True

lista = [
    [1, 2, 3, 4],
    [2, 5, 7, 8],
    [3, 7, 7, 0],
    [4, 8, 0, 8]
]

print(simetrica(lista))