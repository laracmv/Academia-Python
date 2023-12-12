

itens = [9, 6, 7, "Banana", 4.5, True, ["Ola", "World"]]
inversa = [] 

for item in range(len(itens) - 1, -1, -1):
    inversa.append(itens[item])
print(inversa)