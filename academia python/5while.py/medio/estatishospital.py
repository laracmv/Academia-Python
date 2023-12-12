crianca = 0
total = 0
adolescente = 0
jadulto = 0
adulto = 0
vadulto = 0
idoso = 0
n = 1
while n >= 0:
    n = int(input("Digite sua idade: "))
    if n < 0:
        break
    total += 1
    if n >= 0 and n <= 11:
        crianca += 1
    elif n >= 12 and n <= 17:
        adolescente += 1
    elif n >= 18 and n <= 25:
        jadulto += 1
    elif n >= 26 and n <= 35:
        adulto += 1
    elif n >= 36 and n <= 59:
        vadulto += 1
    else:
        idoso += 1

if crianca > 0:
    print(f"0-11 anos: {(crianca/total)*100:.2f} %")
else:
    print("0-11 anos: 0.00 %")
if adolescente > 0:
    print(f"12-17 anos: {(adolescente/total)*100:.2f} %")
else:
    print(f"12-17 anos: 0.00 %")
if jadulto > 0:
    print(f"18-25 anos: {(jadulto/total)*100:.2f} %")
else:
    print("18-25 anos: 0.00 %")
if adulto > 0:
    print(f"26-35 anos: {(adulto/total)*100:.2f} %")
else:
    print("26-35 anos: 0.00 %")
if vadulto > 0:
    print(f"36-59 anos: {(vadulto/total)*100:.2f} %")
else:
    print("36-59 anos: 0.00 %")
if idoso > 0:
    print(f"Acima de 60 anos: {(idoso/total)*100:.2f} %")
else:
    print("Acima de 60 anos: 0.00 %")
