palavra = None
lista = []
i=0
while palavra != 'fim':
    
    palavra = input("Diga sua palavra: ")
    if palavra[0] == "a":
        lista.append(palavra)
        print(lista[i])
        i+=1
    

