def palavras_sao_iguais(palavra):
    listapalavra = palavra.split("-")
    if len(listapalavra) < 2:
        return False
    else:
        if listapalavra[0] == listapalavra[1]:
            return True
        return False
print(palavras_sao_iguais("lara-lara"))
