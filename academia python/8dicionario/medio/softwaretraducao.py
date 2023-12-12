def traduz(lingles,eng2port):
    listapt = []
    for i in lingles:
        for key, value in eng2port.items():
            if i == key:
                listapt.append(value)
    return listapt

palavras = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple'] 
dic =  {'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'}
print(traduz(palavras,dic))

def traduz(lingles, dic):
    l = []
    for palavra in lingles:
        traducao = dic[palavra]
        l.append(traducao)
    return l

p = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']

d = {'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'}

print(traduz(p,d))
