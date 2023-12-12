lista = [
    'banana', 2,5.6,
    'parafuso', 4, 0.15,
    'arroz', 2, 30.10
]

soma = 0
i = 0

lista[6] = "arroz integral"
# trocar item 

while i< len(lista):
    produto = lista[i]
    qtd = lista [i + 1]
    precounit = lista [i + 2]
    precoitem = qtd * precounit
    soma +=precoitem
    print(f'{produto}: {precoitem}')
    i+=3
print(f'{soma:.2f}')

