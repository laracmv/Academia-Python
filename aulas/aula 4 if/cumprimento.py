a = int(input("Que horas sao?"))


if a>0 and a<6:
    print("Boa Madrugada!")
    print(f"São {a} horas!")

elif a>=6 and a<12:
    print("Bom dia!")
    print(f"São {a} horas!")

elif a ==17:
    print("Chá da tarde!")
    print(f"São {a} horas!")

elif a >=12 and a<18:
    print("Boa tarde")
    print(f"São {a} horas!")




elif a>18 and a<24:
    print("Boa noite!")
    print(f"São {a} horas!")

else:
    print("Erro!")


