# media e informar se a pessoa passou ou nao

n1 = float(input("Diga sua nota:"))
n2 = float(input("Diga sua nota:"))
media = (n1+n2)/2
situacao="reprovado"

if media > 7:
    situacao="aprovado"

print(f"media: {media} - {situacao}")
# Obs: caso pule uma linha e fuja da identação ele executará a proxima linha (no caso print("Reprovado")) em caso de print("Aprovado") seja falso!