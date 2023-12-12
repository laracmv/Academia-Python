km = float(input("Diga quanto voce quer percorrer: "))


if km < 0:
    passagem = "Erro"
elif km <= 200:
    passagem = km *.5
else:
    passagem = 100 + (km-200)*.45

print("%.2f"% passagem)

