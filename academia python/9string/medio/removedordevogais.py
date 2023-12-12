def remove_vogais(palavra):
    novapalavra = palavra
    for letra in palavra:
        if letra in "aeiouAEIOU":
            novapalavra = novapalavra.replace(letra, "")
    return novapalavra

print(remove_vogais("remove vogais"))