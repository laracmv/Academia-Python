numero = int(input("Digite seu numero:"))

if (numero%3 == 0 and numero%2 == 0):
    print("Insper")

elif(numero%3) == 0:
        print("Per")

elif (numero%2) == 0:
        print("Ins")

else: 
    print(numero)