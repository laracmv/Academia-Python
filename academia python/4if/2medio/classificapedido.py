# Antes de resolver este exercício, leia completamente o enunciado do EP1!

# Sua tarefa é criar uma função que receba cinco argumentos com informações sobre um pedido, nesta ordem:

# um número real indicando o valor do pedido;
# um número inteiro indicando há quantos dias o pedido está atrasado;
# uma string p/gindicando se o tamanho do pedido é pequeno ou grande;
# uma string s/n indicando se foram identificadas avarias no transporte do pedido;
# uma string s/n indicando se o destino do pedido é para uma capital.
# Você deve devolver uma string representando a classificação do item (reclamacao, normal ou justica) conforme as regras da árvore de decisão:

# Árvore de decisão
# Árvore de Decisão a ser Implementada!
# CLIQUE AQUI para ver a Imagem da Árvore de Decisão.

# Atenção:

# Faça o retorno conforme solicitado: tudo minúsculo e sem acentuação!
# Uma reclamacao representa um pedido que gera um ticket de reclamação (o cliente abre um chamado para reclamar de algo), gerando gastos consideráveis para a empresa
# Um pedido normal representa um pedido onde houve sucesso na entrega e não gera demais problemas, sem gastos extras para a empresa
# Um pedido justica representa um pedido que gerou um processo na justiça, gerando gastos imensos para a empresa
# As entradas do tamanho, capital e avarias poderão vir tanto em minúsculo quanto em maiúsculo!
# O nome da sua função deve ser classifica_pedido

def classifica_pedido(valor, dias_atraso, tamanho, avaria, capital):
    if valor <= 1000.0:
        if dias_atraso <=1:
            if valor <= 150.0:
                if avaria == 'N' or avaria =="n":
                    return "normal"
                else: 
                    return "reclamacao"
            else: 
                return "reclamacao"
        else: 
            return "reclamacao"
    else: 
        if dias_atraso <=10:
            if avaria =="N" or avaria =='n':
                if valor <= 10000.0:
                    if valor <=5000.0:
                        if capital == "N" or capital =='n':
                            return "normal"
                        else: 
                            if tamanho == "P" or tamanho == 'p':
                                return "reclamacao"
                            else:
                                return "normal"
                    else: 
                        return "reclamacao"
                else:
                    return "justica"
            else: 
                return "justica"
        else: 
            return "justica"


print(classifica_pedido(25.98, 0,'g',"n", "N" ))


        