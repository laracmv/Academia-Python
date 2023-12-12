# Validação de entrada de dados é sempre importante para manter a integridade dos dados utilizados em cálculos e processos internos. No contexto do uso de dados de valores monetários, faça um programa que:

# 1 abra um terminal para que o usuário possa digitar um valor;
# 2 o usuário deve entrar apenas com valores positivos decimais ou inteiros;
# 3 se o valor não atender ao item 2, então, imprimir no console erro de entrada e retorne ao passo 1;
# 4 se o usuário não digitar valor algum, apenas der <enter>, então imprimir no console "errro de entrada" e retorne ao passo 1
# se o valor for válido, então, imprimir o valor digitado.
valor = -1
while valor < 0:
    valor = input("Digite seu valor")
    if valor == "":
        print(-1)
        break
    else:
        valor = float(valor)
        if valor > 0:
            print(valor)
        else:
            print("erro de entrada")

# Outra forma
i = True
while i == True:
    valor = input('Digite um valor: ')
    if valor == "":
        print(-1)
        i = False
    elif float(valor) <= 0:
        print('erro de entrada')
    else:
        print(valor)
        i = False