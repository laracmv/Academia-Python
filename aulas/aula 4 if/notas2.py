n1 = float(input("Diga sua nota:"))
n2 = float(input("Diga sua nota:"))
faltas = float(input("Digite o numero de faltas"))
limite=10

media = (n1+n2)/2

situacao="reprovado"

if media >= 5 and faltas <=10:
    situacao="aprovado"

if media < 5:
    situacao = "Reprovado por nota"  

if media <=5 and faltas >10:
    situacao = "Reprovado por nota e falta"

if faltas >10:
    situacao= "Reprovado por faltas"

print(f"media: {media} - {situacao}")