# Você sempre estuda até tarde para DesSoft e, a fim de economizar tempo, sempre pede uma pizza na pizzaria ao lado do Insper. Para ajudar a calcular o preço da pizza, desenvolva um programa que faça as seguintes perguntas, na ordem:

# "Tamanho [P/M/G]? "
# "Borda recheada [S/N]? "
# "Adicional de queijo [S/N]? "
# "Refrigerante [S/N]? "
# "Sobremesa [S/N]? "
# O preço é calculado de acordo com a tabela:

# P	M	G	S
# Tamanho	50.00	70.00	90.00	
# Borda recheada				+15%
# Adicional de queijo				+10%
# Refrigerante				12.00
# Sobremesa			-7% 1	20.00
# No final, o programa deve imprimir o preço total da pizza, formatado com duas casas decimais exatamente.

# 1: Toda pizza tamanho G que tiver sobremesa, ganha desconto de 
# 7
# %
# 7% no preço total.

# Acréscimos: Os valores de acréscimos percentuais são sobre o valor do tamanho da pizza.

# ATENÇÃO: O usuário irá digitar "P", "M" ou "G" para o tamanho da pizza. Para os adicionais, só serão acrescentados se o usuário digitar exatamente "S" quando perguntado do acréscimo.


tamanho = input("Tamanho [P/M/G]?")
borda = input("Borda recheada [S/N]? ")
queijo = input("Adicional de queijo [S/N]? ")
refri = input("Refrigerante [S/N]? ")
sobremesa = input("Sobremesa [S/N]? ")


if tamanho == "P":
    tam = 50.00 
elif tamanho == "M":
    tam = 70.00
else:
    tam = 90.00

if borda == "S":
    bor = tam * 0.15
else:
    bor = 0

if queijo == "S":
    que = tam * 0.1
else:
    que = 0

if refri == "S":
    ref = 12.00
else:
    ref = 0

if sobremesa == "S":
    sobre = 20.00
else:
    sobre = 0

total = tam + bor + que + ref + sobre

if sobremesa =="S" and tamanho == "G":
    total *= 0.93

print (total)