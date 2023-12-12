def fibonacci(n):
    if n==0:
        return  []
    if n == 1:
        return [1]
    lista = [1,1]
    for i in range(3, n+1):
        lista.append(lista[i-1] + lista[i-2])
    print(lista)

print (fibonacci(0))
print (fibonacci(1))
print (fibonacci(2))


