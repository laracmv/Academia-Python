def login_disponivel(login, lista):
    if login not in lista:
        return login
    else:
        i = 0
        while i < len(lista):
            if i == 0:
                if login not in lista:
                    return login
            else:
                i = str(i)
                if login + i not in lista:
                    return login + i
            i = int(i)
            i+=1
        

palavra = "lucio"
l = ['andre', 'fabio', 'lucio','lucio1' ]
print(login_disponivel(palavra, l))

