# Número primos são essenciais para aplicações que envolvem criptografia, por exemplo, o algoritmo RSA faz uso de números primos como base de seu algoritmo criptográfico. A tarefa de achar números primos não é fácil e deve ser automatizada.

# Faça uma função que receba dois valores inteiros positivos e retorne um número primo aleatório no intervalo entre esses dois números. Ou seja, o seu algoritmo deve ficar sorteando números no intervalo e retornar o primeiro primo que encontrar.

# Restrições:

# assumir que o primeiro argumento é sempre menor que o segundo argumento, ou seja,  n1<n2 ;
# o intervalo é fechado, ou seja, inclui os valores de início e fim,  [n1;n2] ;
# o intervalo entre os números DEVE ser de no mínimo 1000, isto é, dados os números  n1  e  n2 , considere que  (n2−n1)≥1000 , caso contrário, o retorno deverá ser erro de intervalo, vide exemplo;
# o primeiro argumento deve ser maior que  1 , caso contrário, o retorno deverá ser erro de intervalo, vide exemplo.
# OBRIGATÓRIO o uso da função random.randint
# você pode, de maneira opcional, fazer uma função para verificar se é primo, porém, certifique-se que o tempo para execução dessa função é adequada ao problema

import random

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def gerarnprimo(n1,n2):
    if n2-n1 <1000 or n1 < 1:
        return 'erro de intervalo'
    else:
        primo = "nao"
        while primo == "nao":
            novonumero = random.randint(n1,n2)
            if eh_primo(novonumero):
                primo = "sim"
        return novonumero

print(gerarnprimo(1,1001))

#----Professor

import random

def ehprimo(n):
    primo = n == 2 or (n != 2 and n % 2 != 0)
    div = 3
    while primo and div <n:
        primo = n % div != 0
        div += 2
        return primo

def sorteiaprimo(a,b):
    if b - a < 1000 or a > 2:
        return 'erro de intervalo'
        x = 0
        while not ehprimo(x):
            x = random.radint(a,b)
        return x

print(sorteiaprimo(500,6000))