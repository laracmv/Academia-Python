def valida_senha(senha):
    caracteres = "?!@#$%&*"
    especial = []
    for elemento in caracteres:
        if elemento in senha:
            if elemento not in especial:
                especial.append(elemento) 
    
    i = 0
    while i<len(senha) - 1:
        if senha[i] == senha[i+1]:
            return False
        i+=1
    
    if len(especial) > 1 and len(senha)>7:
        return True 
    return False

print(valida_senha('@abcdefgh@#'))
    


