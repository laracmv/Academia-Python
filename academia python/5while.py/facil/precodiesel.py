# Estamos em um período de alta volatilidade no preço dos combustíveis. Então, foi solicitado que você construa um programa que analisa os dados históricos do preço do Diesel e produz resultados de interesse.

# O programa deve solicitar a quantidade de dias que se quer analisar, em seguida, solicite o preço do Diesel obervado em cada dia.

# Como saída, o seu programa deve imprimir as seguintes informaçẽos:

# O preço médio do Diesel no período (com duas casas decimais)
dias = int(input("Diga a quantidade de dias a ser analisada:"))
i=0
soma=0
while dias != i:
     preco=float(input("Digite o preco: "))
     soma+=preco
     i+=1
media= soma/dias
print(f"O preço médio cobrado foi de {media:.2f}")