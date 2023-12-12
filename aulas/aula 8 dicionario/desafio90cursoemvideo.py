n = input("Diga seu nome: ")
m = float(input("Diga sua média: "))
if m < 7: 
    s = "reprovado"
else:
    s = "aprovado"

dicionario = {}
dicionario['nome'] = n
dicionario['media'] = m
dicionario['situacao'] = s
print(dicionario)