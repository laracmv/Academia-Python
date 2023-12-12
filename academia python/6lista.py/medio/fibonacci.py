def calcula_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        lista = [0] * n
        lista[0] = 1
        lista[1] = 1
        i = 2
        while i < len(lista):
            lista[i] = lista[i-1] + lista[i-2]
            i += 1
        return lista

print(calcula_fibonacci(3))