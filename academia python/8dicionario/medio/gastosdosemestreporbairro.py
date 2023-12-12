def total_do_semestre_por_bairro(gastos12):
    gastos6 = {}
    for bairros, value in gastos12.items():
        lista = value
        i = 6
        while i<12:
            if bairros not in gastos6:
                gastos6[bairros] = lista[i]
            else:
                gastos6[bairros] += lista[i]
            i+=1
    return gastos6

teste = {
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}

print(total_do_semestre_por_bairro(teste))



