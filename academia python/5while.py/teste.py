# ver o que ta errado: video https://www.youtube.com/watch?v=XCb8jSUcfsc
import random

VALOR_MAXIMO = 20
MAX_TENTATIVAS = 5

num_secreto = random.randint(1, VALOR_MAXIMO)

num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO))) 
while num_chute < 1 or num_chute > VALOR_MAXIMO:
    print("Valor invalido")
    num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO)))

contador = 1

while num_chute != num_secreto and contador < MAX_TENTATIVAS:
    contador += 1
    
    if num_chute <num_secreto:
        print("Muito baixo")
    elif num_chute > num_secreto: 
        print("Muito alto")

    num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO)))
    while num_chute < 1 or num_chute > VALOR_MAXIMO:
        print("Valor invalido")
        num_chute = int(input("Digite inteiro entre 1 e {0}: ".format(VALOR_MAXIMO)))

if num_chute != num_secreto:
    print("Que pena, você perdeu!")
else:
    print("Acertou em {0} tentativas".format(contador))
