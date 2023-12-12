# Sua tarefa é criar uma função que calcule e retorne o valor de um lanche.

# Ela recebe, nesta ordem:

# Tipo do pão: string "australiano" ou "brioche".
# Australiano custa R$ 5,25.
# Brioche custa R$ 7,00.
# Quantidade de carnes: inteiro que define quantas carnes serão utilizadas no lanche.
# A primeira carne custa R$ 8,00.
# As demais custam R$ 5,00.
# Salada: string "S" ou "N" indicando se o lanche terá salada.
# Cobre R$ 3,00 pela salada.
# Bacon: string "S" ou "N" indicando se o lanche terá bacon.
# Cobre R$ 7,50 pelo bacon.
# Molho: string "S" ou "N" indicando se o lanche terá molho.
# Cobre R$ 1,00 pelo molho.
# Queijo: string "S" ou "N" indicando se o lanche terá queijo.
# Cobre R$ 5,40 pelo queijo.
# Ainda, considere um desconto de 5% se o valor do lanche for acima de R$ 33,00.

# Exemplo 1:

# Entradas (como argumentos da função):
# Tipo do pão: "brioche"
# Quantidade de carnes: 1
# Salada: "N"
# Bacon: "N"
# Molho: "N"
# Queijo: "S"
# Saída: 20.4 (retorno da função)
# Entendendo:
# 7 pelo pão, 8 pela carne e 5.4 pelo queijo
# Exemplo 2:

# Entradas (como argumentos da função):
# Tipo do pão: "australiano"
# Quantidade de carnes: 3
# Salada: "S"
# Bacon: "S"
# Molho: "S"
# Queijo: "S"
# Saída: 38.1425
# O nome da sua função deve ser calcula_preco_hamburguer

def calcula_preco_hamburguer(pao, quantcarne, salada, bacon, molho, queijo):
    total = 0 

    if pao == "australiano":
        total += 5.25
    else:
        total += 7.00
    
    if quantcarne >= 1:
        total += 8.00
        if quantcarne >1:
            total += 5.00 * (quantcarne - 1)
        else:
            total = total
        
    
    if salada == "S":
        total += 3.00
    else:
        total = total
    
    if bacon == "S":
        total += 7.50
    else:
        total = total
    
    if molho == "S":
        total += 1.00
    else:
        total = total
    
    if queijo == "S":
        total += 5.40
    else:
        total = total
    
    if total > 33.00:
        total *= 0.95
    else: 
        total = total
    
    return total

print(calcula_preco_hamburguer("australiano", 2,'S', "S", "S","S"))