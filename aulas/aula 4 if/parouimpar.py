def ehPar(x):
    if (-1)**x > 0:
        return True
    else:
        return False

def ehPar2(x):
    if x%2 ==0:
        return True

    else:
        return False

valor = int(input("Digite seu valor: "))
if ehPar(valor):
    print("É par")
else:
    print("não é par")
    # Obs: no 1o if, ele será executado se o resultado do return for verdadeiro! Caso nao, o else ocorrerá