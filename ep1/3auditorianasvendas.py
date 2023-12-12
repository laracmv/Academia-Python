# Aqui é onde todo o EP é integrado, onde as funções desenvolvidas nos exercícios são utilizadas. O sistema de automação de auditoria irá sempre receber dois valores, valor desejado e valor da venda, que são informações de amostras de vendas que ocorreram na Loja. O valor desejado é o valor mínimo da venda e o valor da venda é o preço de fato praticado para a venda. O sistema de auditoria deverá fazer estatísticas das amostra coletadas e dizer se há suspeita de anomália ou não.

# O programa deverá solicitar valores desejados e de vendas até que algum dos dois seja em branco ( vazio), quando isso ocorrer o dado dessa venda não será considerada, eg., se o usuário não digitar valor desejado, o programa sequer irá perguntar o valor de venda (exemplo 1); no caso do usuário digitar um valor desejado e deixar de preencher o valor de venda, então, deverá desconsiderar a venda, inclusive o valor desejado recém digitado (exemplo2).

# Exemplo 1:

# valor desejado: 40
# valor da venda: 40
# valor desejado: 50
# valor da venda: 57
# valor desejado: 60
# valor da venda: 48
# entradas desconsideradas pois valor desejado maior que o valor da venda, tente novamente!
# valor desejado: 90
# valor da venda: 90
# valor desejado: 100
# valor da venda: 104
# valor desejado: 
# MÉDIA: desejado [70.00] venda [72.75]
# DESVIO PADRÃO AMOSTRAL: desejado [29.44] venda [29.41]
# Anomalia: SIM


import math
vd = []
vv = []
somavd = 0
somavv = 0
n = 0

while vd != "" and vv != "":
    vdesejado = input("valor desejado: ")
    if vdesejado != "":
        vvenda = input("valor de venda: ")
        if vdesejado != "": 
            vdesejado = float(vdesejado)
        if vvenda != "":
            vvenda = float(vvenda)
            if vdesejado > vvenda:
                print("entradas desconsideradas pois valor desejado maior que o valor da venda, tente novamente!")
            else:
                vd.append(vdesejado)
                vv.append(vvenda)
                somavd += vd[n]
                somavv += vv[n]
                n +=1
    else:
        break

mediavd = somavd/n
mediavv = somavv/n
print(f"MÉDIA: desejado [{mediavd:.2f}] venda [{mediavv:.2f}]")

def desviopadrao(vd,media):
    part1 = 1/(len(vd) - 1)
    i = 0
    somatorio = 0
    while i < len(vd):
        somatorio+= (vd[i] - media)**2
        i +=1
    desvio = math.sqrt(part1 * somatorio)
    return desvio

desviovdesejado = desviopadrao(vd,mediavd)
desviovvenda = desviopadrao(vv, mediavv)

print(f"DESVIO PADRÃO AMOSTRAL: desejado [{desviovdesejado:.2f}] venda [{desviovvenda:.2f}]")

def distancia(listavdesejada, listavvenda):
    part1 = 1/len(listavdesejada)
    i = 0
    somatorio = 0
    while i < len(listavdesejada):
        somatorio += (listavdesejada[i] - listavvenda[i])**2
        i+=1
    erro = math.sqrt(part1 * somatorio)
    return erro

distancia = distancia(vd, vv)

if distancia > 0.05*mediavd:
    print("Anomalia: SIM")
else:
    print("Anomalia: NÃO")