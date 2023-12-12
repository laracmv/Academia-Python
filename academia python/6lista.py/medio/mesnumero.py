lista = ["janeiro","fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
nome = input("Diga o nome do mês: ")

i = 0

while i < len(lista):
    if lista[i] == nome:
        print(i+1)
        break
    i+=1