# criando uma funçao e chamando ela!


def celsius2fah(c):
    f = c * 9/5 + 32
    return f
    # return é necessario pq outros valores podem ter dentro da funcao e nao necessariamente ser utilizado
     
temperatura = 26
tempF = celsius2fah(temperatura)
print(f"{temperatura}C -> {tempF}f")
# f = .format de forma mais simplificada