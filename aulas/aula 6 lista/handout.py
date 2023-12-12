disciplinas = ["lara", "lara2", 2]

print(disciplinas)
print(disciplinas[0])
print(len(disciplinas))

# substituir elementos

a = [1, 2, 5, 7]

a[1] = 3

#deletar elementos
frutas = ['banana', 'maçã', 'alface', 'pêssego']
print(frutas)

del frutas[2]
print(frutas)

#apagar ultimo item lista
lista.pop()

#adicionar um item no fim da lista:

frutas.append('pêra')
print(frutas)

#Somar e multiplicar listas:
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_1_e_2 = lista_1 + lista_2
print(lista_1_e_2)  
# Vai imprimir [1, 2, 3, 4, 5, 6]

lista_2_e_1 = lista_2 + lista_1
print(lista_2_e_1) 
# Vai imprimir [4, 5, 6, 1, 2, 

numeros = [1, 2, 3]
numeros_vezes_3 = numeros * 3  # Análogo a: numeros + numeros + numeros
print(numeros_vezes_3)  # Vai imprimir [1, 2, 3, 1, 2, 3, 1, 2, 3]      

# anteriores

#inverter lista
minha_lista = [1, 2, 3, 4, 5]
lista_invertida = minha_lista[::-1]

print(lista_invertida)

#inserir elemento em qualquer posicao
minha_lista = [2, 3, 4, 5]
elemento = 1  # Elemento que você deseja adicionar no início da lista
minha_lista.insert(0, elemento)

print(minha_lista)

#pegar ultimo elemento de lista
lista = [1,2,3]
print(lista[-1])