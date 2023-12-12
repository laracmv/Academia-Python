def contabiliza(dicionario):
    dinovo = {}
    for key,value in dicionario.items():
      for items in value:
        espaco = items.find(" ")
        numero = items[:espaco]
        nomes = items.replace(numero, "")
        numero = int(numero)
        nomes = nomes.strip()
        if nomes not in dinovo:
            dinovo[nomes] = numero
        else:
            dinovo[nomes] += numero
    return  dinovo

dic = {
    'joaquim': [
        '02 caixa de bananinha',
        '3 carrinho',
        '4 refrigerante'
    ],
    'joana': [
        '2 carrinho',
        '3 quebra-cabeça',
        '1 caixa de cocada'
    ],
    'sebastião': [
        '1 refrigerante',
        '1 quebra-cabeça'
    ],
}

print(contabiliza(dic))



