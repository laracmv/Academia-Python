matriz_letras = [[]]

# Seu primeiro palpite
palpite1 = "ABCD"

# Adicione as letras do primeiro palpite na matriz
for letra in palpite1:
    matriz_letras[-1].append(letra)

# Seu segundo palpite
palpite2 = "EFGH"

# Crie uma nova linha para o segundo palpite
matriz_letras.append([])

# Adicione as letras do segundo palpite na nova linha
for letra in palpite2:
    matriz_letras[-1].append(letra)

# Imprima a matriz
for linha in matriz_letras:
    print(' '.join(linha))
