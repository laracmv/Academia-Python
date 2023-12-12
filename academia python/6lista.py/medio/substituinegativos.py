def zera_negativos(x):
    i =0
    while i < len(x):
        if x[i]<0:
            x[i] = 0
        else:
            x[i]=x[i]
        i+=1
    return x