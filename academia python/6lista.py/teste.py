def verifica_pais(nome_pais, lista_de_paises):
    return nome_pais in lista_de_paises

# Exemplo de uso:
lista_de_paises =[
    ['libia', 3678],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]
pais = 'libia'
esta_na_lista = verifica_pais(pais, lista_de_paises)
print(esta_na_lista)