# Durante o processo seletivo para vagas de emprego, é comum que existam dinâmicas e testes nos quais o candidato recebe uma nota conforme seu desempenho.

# Certa empresa deseja avaliar os candidatos com base em três etapas. Você foi encarregado de construir um programa para analisar os resultados destas etapas e selecionar os candidatos aptos a passar para a próxima fase.

# Sua função deve receber dois parâmetros (nesta ordem): uma lista de candidatos e uma lista de criterios.

# Na lista de candidatos, cada elemento desta lista contém uma outra lista com as informações do candidato. Nesta segunda lista (interna):

# A primeira posição contém o nome do candidato
# A segunda posição contém o número RG do candidato em formato string
# A terceira posição contém uma outra lista, idealmente com três notas tiradas pelo candidato.
# Já a lista de critérios tem três notas mínimas que os candidados devem atingir em cada uma das três provas para serem aptos a prosseguir no processo seletivo.

# Sua função deve retornar uma lista contendo sublistas contendo apenas o nome e RG daqueles candidatos considerados aptos.

# OBS:

# Caso a lista de candidados seja vazia, retorne uma lista vazia.
# Candidatos que devem ser selecionados são aqueles que possuem exatamente três notas na lista de notas (precisa validar), além de obedecerem os critérios de nota mínima (nota igual ao critério também habilita!).
# Os critérios estão em ordem, ou seja, a pri---meira nota do candidato deve obedecer ao primeiro critério e assim por diante.
# Alguns candidatos estão com a lista de notas inconsistente (menos que ou mais que três notas), estes candidatos devem ser ignorados.
# Já o nome e o RG de cada candidado sempre estarão disponíveis (não precisa validar).
# Considere que as notas sempre estarão no intervalo fechado [0..10], também não é necessário fazer esta validação.
# Você deve manter a ordem dos candidatos (entre a lista de candidatos e aqueles que aparecem na lista de aprovados).

def seleciona_candidatos(candidatos, criterios):
    aprovados = []
    i = 0
    if candidatos == []:
        return []
    else:
        while i < len(candidatos): 
            if len(candidatos[i][2]) == 3 and candidatos[i][2][0] >= criterios[0] and candidatos[i][2][1] >= criterios[1] and candidatos[i][2][2] >= criterios[2]:
                candaprovado = [candidatos[i][0], candidatos[i][1]]
                aprovados.append(candaprovado)
            i+=1
    return aprovados



