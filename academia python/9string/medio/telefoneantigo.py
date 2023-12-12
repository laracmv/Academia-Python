def atualiza_telefone(nantigo):
    if "-" in nantigo:
        tracoremovido = nantigo.replace("-", "")
        if len(tracoremovido) == 8:
            novo = "9" + nantigo
            return novo
        elif len(tracoremovido) ==9:
            return nantigo
    if len(nantigo) == 8:
        novo = "9" + nantigo
        return novo
    elif len(nantigo) == 9:
        return nantigo

numero = "88888888"
print(atualiza_telefone(numero))


