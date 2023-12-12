def palavras_com_tamanho_crescente(lista):
    menor = ""
    for palavra in lista:
        if len(menor) < len(palavra):
            menor = palavra
        else:
            return False
    return True

entrada = ['a', 'ab', 'abc', 'abcd']

print(palavras_com_tamanho_crescente(entrada))

