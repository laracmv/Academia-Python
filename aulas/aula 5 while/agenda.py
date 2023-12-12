contatos = []
print("-----------Bom dia-------------")
while True:
    comando = input(">")
    if comando == "exit":
        break
    elif comando == "add":
        n=input("nome? ")
        contatos.append(n)
        # append adiciona no final da lista
        #remove = apaga o primeiro que tiver aquele nome
    elif comando == "list":
        print(contatos)
    else:
        print("Comando invalido")

print("Até logo")