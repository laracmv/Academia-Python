def monta_dicionario(l1, l2):
    i = 0
    dicionario = {}
    while i < len(l2):
        dicionario[l1[i]] = l2[i]
        i+=1
    return dicionario

l1 = ["A", "B", "C"]
l2 = [1,2,3]

print(monta_dicionario(l1,l2))