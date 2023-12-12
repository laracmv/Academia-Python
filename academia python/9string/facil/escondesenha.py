def esconde_senha(senha):
    nova=''
    for letra in senha:
        y=senha.replace(senha,'*')
        nova+=y
    return nova
    
print(esconde_senha('l1 l2'))

def esconde_senha(senha):
    i = 0
    while i < len(senha):
        if i == 0:   
            y = senha.replace(senha, "*")
        else:
            y += senha.replace(senha, "*")
        i+=1
    return y

print(esconde_senha('l1 l2'))