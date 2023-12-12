dicionario = {"janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, "maio": 5, "junho": 6, "julho": 7, "agosto": 8, "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12}

mes = input("Digite seu mes:")

i = 0
while i < len(dicionario):
    if mes in dicionario:
        print(dicionario[mes])
        break
    i+=1

