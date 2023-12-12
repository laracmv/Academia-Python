def junta_nome_sobrenome(nome, sobrenome):
    junto = []
    
    i=0
    while i<len(nome):
        juntos = nome[i] + " " + sobrenome[i]
        junto.append(juntos)
        i+=1
    return junto

lista1 = ["Lara", "Carlos"]
lista2 = ["Vasco", "Celos"]
print(junta_nome_sobrenome(lista1, lista2))