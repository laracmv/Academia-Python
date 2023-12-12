def calcula_segredo(n):
    soma = 0
    if n >=100 and n<= 999:
        soma = n // 100
        # // mostra o valor antes da virgula, que nesse caso seria o 9(floor division)
        n %= 100
        # mostra o resto da divisão, que seria o numero - o primeiro digito. no caso do print, 998 % 100 = 98
        soma += n //10
        n %= 10
        soma += n // 1
        n %=1
        return soma
    else:
        return -1

print(calcula_segredo(998))