# São Paulo é conhecida como a terra da garoa, com chuva, sol e frio podendo acontecer no mesmo dia! Assim, guarda-chuva e casaco compõem o kit paulista, protegendo os locais de qualquer surpresa climática!

# Você deve construir um programa que calcule estatísticas sobre o quão preparado um paulista está para enfrentar o clima nos últimos 
# �
# n dias.

# Solicite ao usuário que informe (nesta ordem):

# Quantos dias quer analisar?
# Para cada dia, pergunte (nesta ordem):
# Choveu [S/N]?
# Temperatura mínima (em Celsius)?
# Tinha guarda-chuva [S/N]?
# Tinha casaco [S/N]?
# Em seguida, você deve imprimir as seguintes saídas:

# Choveu em 10 de 15 dias
# Fez frio em 7 de 15 dias
# Usou guarda-chuva em 8 de 10 dias de chuva
# Usou casaco em 3 de 7 dias de frio
# Notas:

# Considere que fez frio caso a temperatura mínima do dia tenha ficado abaixo de 20 graus Celsius.
# Só deve ser considerado na estatística o uso de guarda-chuvas ou de casaco se, repectivamente, choveu ou fez frio no dia.
# Considere que sempre haverá pelo menos um dia para ser analisado.
# Cuidado, a saída deve ser examente o que está no texto, exceto pelos números.



dias = int(input("Quantos dias para analisar? "))
i = 0
chuva = 0
frio = 0
gc = 0 
cs = 0

while i<dias:
    i+= 1
    
    choveu = input("Choveu [S/N]?")
    tempmin = float(input("Temperatura mínima (em Celsius)?"))
    guardachuva = input("Tinha guarda-chuva [S/N]?")
    casaco = input("Tinha casaco [S/N]?")

    if choveu == "S":
        chuva += 1

    if tempmin <20:
        frio +=1

    if choveu == "S" and guardachuva == "S":
        gc +=1
    
    if tempmin < 20 and casaco == "S":
        cs +=1
    
print(f"Choveu em {chuva} de {dias} dias")
print(f"Fez frio em {frio} de {dias} dias")
print(f"Usou guarda-chuva em {gc} de {chuva} dias de chuva")
print(f"Usou casaco em {cs} de {frio} dias de frio")