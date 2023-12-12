def calcula_valor_liquido(valortotal,ordemdevenda):
    if ordemdevenda =="pyfood":
        valorLiquido = 0.7*valortotal
        return valorLiquido
    if ordemdevenda == "whatsapp":
        valorLiquido= 0.91*valortotal
        return valorLiquido

valor = float(input("Digao o valor total:"))
servico= input("Ordem de serviço: ")
print(calcula_valor_liquido(valor,servico))