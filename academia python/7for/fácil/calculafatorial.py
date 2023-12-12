def fatorial(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= 1 * i
    return fatorial

print(fatorial(3))