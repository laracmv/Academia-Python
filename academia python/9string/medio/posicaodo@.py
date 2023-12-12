def pos_arroba(email):
    for elemento in email:
        if elemento == "@":
            posicao = email.index(elemento)
    return posicao

print(pos_arroba("lara@"))