def calcula_idade(dia1,mes1,ano1,dia2,mes2,ano2):
    if mes1<mes2: 
        idade=ano2-ano1
        return idade
    elif mes1==mes2 and dia1<=dia2:
        idade=ano2-ano1
        return idade
    elif mes1==mes2 and dia1>dia2:
        idade=ano2 -1 - ano1
        return idade
    else:
        idade=ano2 - 1 - ano1
        return idade
        
