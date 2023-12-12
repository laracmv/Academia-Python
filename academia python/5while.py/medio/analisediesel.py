# Estamos em um período de alta volatilidade no preço dos combustíveis. Então, foi solicitado que você construa um programa que analisa os dados históricos do preço do Diesel e produza resultados de interesse.

# O programa deve solicitar a quantidade de dias que se quer analisar, em seguida, solicite o preço do Diesel obervado em cada dia.

# Como saída, o seu programa deve imprimir as seguintes informações:

# O melhor dia para compra do combustível (dia com menor preço)
# O pior dia para compra do combustível
# O preço médio do combustível no período (com duas casas decimais)

dias = int(input("Diga a quantidade de dias a ser analisada: "))
i = 0 
preco = 0
min = 0
max = 0
soma = 0

while i < dias:
    preco = float(input("preço"))
    soma += preco
    i+= 1
    if i == 1:
        min = preco
        max = preco
        diamin = i
        diamax = i
    else: 
        if preco < min:
            min = preco
            diamin = i
        if preco > max:
            max = preco
            diamax = i

media = soma/dias
print(f"O dia {diamin} foi o melhor dia para compra")
print(f"O dia {diamax} foi o pior dia para compra")
print(f"O preço médio cobrado foi de {media: .2f}")

