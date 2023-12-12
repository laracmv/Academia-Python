

def mais_frequente(lista):
    dic = {}
    for palavra in lista:
        if palavra not in dic:
            dic[palavra] = 1
        else: 
            dic[palavra] +=1
    maior = 0
    mword = None
    for word, quant in dic.items():
        if quant > maior:
            maior = quant
            mword = word
    return mword

l  = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']

print(mais_frequente(l))