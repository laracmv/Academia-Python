def usuarios_por_pais(lista,dic):
    novodic = {}
    for sigla, pais in dic.items():
        usuarios = []
        for email in lista:
            if sigla in email:
                arroba = email.find("@")
                usuario = email[:arroba]
                usuarios.append(usuario)
        if usuarios != []:
            novodic[pais] = usuarios
    return novodic

teste = ['usuario1@insper.edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br']
testee = {
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia'
}

print(usuarios_por_pais(teste, testee))
