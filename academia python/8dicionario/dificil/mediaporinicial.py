def medias_por_inicial(dic):
    novodic = {}
    contador = {}
    for nome, nota in dic.items():
        letra = nome[0]
        if letra not in novodic:
            novodic[letra] = nota
            contador[letra] = 1
        else:
            novodic[letra] += nota
            contador[letra] +=1
    
    for letter in novodic:
        novodic[letter] = novodic[letter] / contador[letter]
    return novodic

l  ={
    'Andrew Ayres': 6,
    'Fábio Ikeda': 10,
    'Fábio Kurauchi': 9,
    'Raul Hage': 8
 }

print(medias_por_inicial(l))

