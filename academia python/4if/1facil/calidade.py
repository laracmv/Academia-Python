def calcula_aumento(salario):
    if salario <=1250.00:
        aumento= salario*0.15
    else:
        aumento= salario*0.1
        return aumento
    
salario = 1500.00
print(f"seu aumento e: {calcula_aumento(salario): .2f}")