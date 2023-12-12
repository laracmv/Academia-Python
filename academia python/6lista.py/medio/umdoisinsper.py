def produz_um_dois_insper(numero_inicial, numero_final, multiplo):
    i = numero_inicial
    numero = []
    num = numero_inicial

    while i <= numero_final :
            
        if num % multiplo == 0: 
            numero.append("Insper") 
        else:
            numero.append(num)
        num +=1
        i+=1
    return numero

print(produz_um_dois_insper(10,20,4))
    