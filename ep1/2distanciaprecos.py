# Para calcular a distância entre os preços passados pelo usuários, será utilizada a equação de erro médio quadrático. Faça uma função que recebe uma lista com elementos que são listas de dois preços: desejado e venda, nessa ordem. A função criada deve retornar o erro médio quadrático dessa lista de preços.
# O nome da sua função deve ser distancia

import math

def distancia(lista):
    part1 = 1/len(lista)
    i = 0
    somatorio = 0
    while i < len(lista):
        somatorio += (lista[i][0] - lista[i][1])**2
        i+=1
    erro = math.sqrt(part1 * somatorio)
    return erro
