def bairro_mais_custoso(gastos):
    maior = 0
    bairromaior = None
    for bairro, valores in gastos.items():
        i = 6
        soma =0
        while i < 12:
            soma+= valores[i]
            i +=1
        
        if soma > maior:
            maior = soma
            bairromaior = bairro

    return bairromaior

t = {
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}

print(bairro_mais_custoso(t))




    
