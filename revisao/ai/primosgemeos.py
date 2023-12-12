# Na Teoria dos Números, primos gêmeos são dois números primos cuja diferença é igual a dois. Por exemplo, 3 e 5, 5 e 7, 11 e 13, e assim por diante. Como curiosidade, existem cerca de mil números primos gêmeos abaixo de 100.000.

# Considere a série abaixo que tem como termos o inverso de primos gêmeos:

# (13+15)+(15+17)+(111+113)+(117+119)+(129+131)+… 

# Faça uma função que recebe o valor de  n  e retorna o resultado da fórmula acima utilizando  n  pares de primos gêmeos.

# Exemplo:
# Para a entrada #!python n = 2
# (13+15)+(15+17) 
# Retorna:  ≈0.8761904761904762

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gerar_primos_gemeos(n):
    primos_gemeos = []
    num = 3  # Começando a busca a partir do primeiro primo gêmeo (3, 5)
    
    while len(primos_gemeos) < n:
        if eh_primo(num) and eh_primo(num + 2):
            primos_gemeos.append((num, num + 2))
        num += 2
    
    return primos_gemeos


def primogemeo(n):
    gerarprimos = gerar_primos_gemeos(n)
    soma = 0
    for valor in gerarprimos:
        soma += (1/valor[0]) + (1/valor[1])
    return soma

print(primogemeo(5))