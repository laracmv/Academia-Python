# Os hospitais comumente utilizam um sistema de cores para classificar a urgência dos atendimentos, priorizando conforme o risco de vida.

# Considere um sistema de classificação de três cores: Vermelho, Laranja e Azul. Nele, todos os atendimentos Vermelhos devem ser realizados antes dos Laranjas e todos atendimentos Laranjas devem ser realizados antes dos classificados como Azuis.

# Sabendo que um atendimento Vermelho demora 07 minutos, e que cada atendimento Laranja ou Azul demora 05 minutos, crie um programa que pergunte ao usuário (nesta ordem):

# Classificação? (V/L/A)
# Quantos Vermelhos estão aguardando?
# Quantos Laranjas estão aguardando?
# Quantos Azuis estão aguardando?
# Seu programa deve imprimir na saída por quantos minutos o usuário deverá esperar para ser chamado para atendimento. Apenas o número, sem outros textos.

# OBS: um novo paciente sempre vai para o final da fila da sua classificação. Assim, um recém chegado classificado como Vermelho deve esperar todos os vermelhos até ser atendido.

classificacao = input('Classificação?')
vermelhos = int(input("Quantos Vermelhos estão aguardando?"))
laranjas = int(input("Quantos Laranjas estão aguardando?"))
azuis = int(input("Quantos Azuis estão aguardando?"))

if classificacao == 'V':
    tempo = vermelhos * 7 
    print(tempo)
if classificacao == "L":
    tempo = vermelhos * 7 + laranjas * 5
    print(tempo)
if classificacao == "A":
    tempo = vermelhos * 7 + laranjas * 5 + azuis * 5
    print(tempo)
