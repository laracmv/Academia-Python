def conta_letras(s):
    dicionario = {}
    for i in range(len(s)):
        letra = s[i]
        if letra not in dicionario:
            dicionario[letra] =1
        elif i == "":
            dicionario[""] = 1
        else:
            dicionario[letra] += 1
    return dicionario

print(conta_letras("banana nanica"))