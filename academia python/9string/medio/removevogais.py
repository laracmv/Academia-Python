def remove_vogais(string):
    vogais = "aeiou"
    for vogal in vogais:
        string = string.replace(vogal, '')
    return string

minha_string = "exemplo"
string_sem_vogais = remove_vogais(minha_string)
print(string_sem_vogais) 