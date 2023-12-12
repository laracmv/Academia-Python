def capsLock(string):
    string2 = ""
    for letra in string:
        if letra.islower():
            letra = letra.upper()
            string2 += letra
        else:
            letra = letra.lower()
            string2 += letra
    return string2

print(capsLock("LARA"))