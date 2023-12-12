palavra = ''

while palavra != "fim":
    palavra = input("Diga sua palavra: ")
    if palavra == "fim":
        print("Até a próxima")
    else:
        vogais = "aeiouAEIOU"
        for vogal in vogais:
            if vogal in palavra:
                palavra = palavra.replace(vogal,"")
        print(palavra)
