n = 9

for i in range(11):
    # não precisa de contador, menor risco de loop infinito. For so funciona com lista!
    # O range cria uma lista, com o valor i até o valor 11(11 não incluso)
    # se nao colocar argumento, ele sempre começa em zero
    print(f"{n} x {i:02} = {n * i}")


