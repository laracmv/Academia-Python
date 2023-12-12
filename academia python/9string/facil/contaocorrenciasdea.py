def conta_a(stri):
    vezes = 0
    i = 0
    while i < len(stri):
        if stri[i] == "a":
            vezes +=1
        i+=1
    return vezes

print(conta_a("lara"))


