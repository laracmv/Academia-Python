def extrai_nomes_de_usuarios(lista):
    lemail = []
    for email in lista:
        posicao = email.find("@")
        usuario = email[:posicao]
        lemail.append(usuario)
    return lemail

print(extrai_nomes_de_usuarios("lara@gmail"))

