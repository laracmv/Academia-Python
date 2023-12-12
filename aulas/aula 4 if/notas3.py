n1 = float(input("Diga sua nota:"))
n2 = float(input("Diga sua nota:"))
faltas = float(input("Digite o numero de faltas"))
limite=10

media = (n1+n2)/2

situacao="reprovado"

if media >= 5:
    if faltas <=limite:
        print("Aprovado")
    else:
        print("Reprovado por faltas")

else:
    if faltas <=limite:
        print("Reprovado por nota")
    else:
        print("Reprovado por nota e faltas")

print(f"media: {media} - {situacao}")