def classifica_idade(idade):
    if idade > 0:
        if idade <=11:
            idade = "crianca"
        elif idade >11 and idade<=17:
            idade = "adolescente"
        else: 
            idade ="adulto"
    else:
        idade = "Erro"

idade = input("Digite idade:")
idade = classifica_idade(idade)
print(idade)