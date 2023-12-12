# Ao final do semestre, um professor desejou fazer uma análise das notas alcançadas pelos alunos nas avaliações intermediária e final aplicadas durante sua disciplina, bem como das respectivas médias finais obtidas. A média é ponderada, tendo a AI peso de 40% e a AF de 60%.

# O professor te contratou para desenvolver um programa no qual ele pode inserir as notas individuais obtidas nas avaliações e, ao final, obter uma análise. O programa deve perguntar:

# "Deseja inserir um novo aluno? [S/N]"
# Sempre que a resposta for 'S', o programa deve perguntar as notas obtidas:

# "Qual a nota na AI? "
# "Qual a nota na AF? "
# Quando a resposta for 'N', o programa deve parar e imprimir as seguintes informações:

# A menor nota obtida em avaliações
# A maior média final alcançada
# A média das notas da AI
# A média das notas da AF
# Exemplo de entrada (valores informados pelo usuário):

# Deseja inserir um novo aluno? S
# Qual a nota na AI? 4.5
# Qual a nota na AF? 7
# Deseja inserir um novo aluno? S
# Qual a nota na AI? 7.5
# Qual a nota na AF? 8.5
# Deseja inserir um novo aluno? N
# Exemplo de saída:

# "A menor nota em avaliações foi 4.5"
# "A maior média final foi 8.1"
# "A média das notas da AI foi 6.0"
# "A média das notas da AF foi 7.8"
# OBS:

# suponha que sempre haverá pelo menos um aluno;
# utilize um print por informação;
# cada valor deve ser impresso com exatamente uma casa decimal;
# É PROIBIDO O USO DE LISTA OU FUNÇÕES QUE OPEREM SOBRE LISTAS PARA ESSE QUIZ.


menornota = 10
# menornota = 10 pq qualquer outra nota seria menor q isso
maiornota = 0
mediaai = 0
mediaaf = 0
qtd = 0

while input("Deseja inserir um novo aluno? [S/N]") == "S":
    ai = float(input("Qual a nota da AI?"))
    af = float(input("Qual a naota na AF?"))
    if ai < menornota:
        menornota = ai
    if af < menornota:
        menornota  = af
    media = ai * 0.4  + af * 0.6
    if maiormedia < media:
        maiormedia = media
        mediaai += ai
        mediaaf += af
        qtd+= 1
mediaai /= qtd
mediaaf /=qtd
print(menornota)
print(maiornota)
print(mediaai)
print(mediaaf)