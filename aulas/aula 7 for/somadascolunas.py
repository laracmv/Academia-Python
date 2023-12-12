# faca uma funcao chamada soma colunas que recebe uma matriz e devolve uma lista com soma das colunas


def somacolunas(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    resultado = [0] * col
    for col in range(ncol):
        for lin in range(nlin):
            resultado[col] += matriz[lin][col]

