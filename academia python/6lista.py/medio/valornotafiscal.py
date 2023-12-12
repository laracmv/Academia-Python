def calcula_total_da_nota(preco, quantidade):
    i = 0
    soma = 0
    while i < len(preco):
        soma += preco[i]*quantidade[i]
        i+=1
    return soma
