# Um determinado Cassino em Las Vegas precisa de um sistema para simular a contabilização de ganhos e perdas num determinado jogo de dados. O jogo consiste em adivinhar qual das seis faces de um dado irá ficar com a face para cima após o dado ser lançado de forma aleatória sobre uma mesa.

# Você deve implementar uma função que simula os ganhos e perdas desse jogo. O jogo funciona da seguinte maneira: o jogador escolhe um número da sorte, um valor para aposta e o número de rodadas que irá simular, passando então esses valores, nessa ordem, como parâmetros para a função de simulação que você vai criar.

# A cada rodada um número é sorteado, entre 1 e 6. Se o número da sorte for igual ao número sorteado, então, o valor da aposta é aumentado em 1/3; caso contrário, se os números forem diferentes, então o valor da aposta é decrescido em 1/6. O valor inicial da aposta da próxima rodada é o valor resultante da rodada anterior, sendo o número total de rodadas é dada pelo usuário.

# Ao final de todas as rodadas, a função deve retornar o valor total do apostador após os ganhos e perdas de todas as rodadas.

# Exemplo

# Entradas:

# número da sorte escolhido: 5
# valor da aposta inicial: 180.00
# número total de rodadas: 3
# Rodadas:

# rodada:
# número sorteado: 3
# valor da aposta corrigido: 150.00
# rodada:
# número sorteado: 5
# valor da aposta corrigido: 200.00
# rodada:
# número sorteado: 1
# valor da aposta corrigido: 166.67
# Saída:

# valor do apostador: 166.66666...
# Nota: o usuário irá escolher apenas valores inteiros para o número da sorte escolhido e para o número de rodadas, porém, pode escolher números com decimais para o valor inicial da aposta. O retorno da função é um número com casas decimais.

# O nome da sua função deve ser apostando_em_dados

import random

def apostando_em_dados(numerosorte, valor, rodadas):
    i = 0
    while i<rodadas:
        n = random.randint(1,6)
        i+=1
        if numerosorte == n:
            valor += 1/3 * valor
        else: 
            valor -= 1/6 * valor
    return valor