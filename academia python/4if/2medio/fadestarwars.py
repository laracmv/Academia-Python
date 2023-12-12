# Você recebeu a importante tarefa de ranquear os fãs de Star Wars. Para isso, desenvolva um programa que faz 5 perguntas sobre Star Wars para o usuário. As perguntas são:

# "Já assistiu todos os filmes?"
# "Tem camiseta temática?"
# "Já se fantasiou de algum personagem?"
# "Tem algum action figure/nave/etc?"
# "Já foi no Galaxy's Edge, o parque temático da franquia?"
# No final, o programa deve emitir uma classificação sobre a participação da pessoa no universo Star Wars. Se a pessoa responder positivamente (digitar exatamente a resposta "sim") a 2 questões a pessoa deve ser classificada como "Padawan", entre 3 e 4 como "Jedi" e 5 como "One with the Force". Caso contrário, ela será classificada como "Inocente".


sim = 0
nao = 0

assistiu = input("Já assistiu todos os filmes?")

if assistiu == "sim":
    sim +=1
else: 
    nao +=1

camisa = input("Tem camiseta temática?")

if camisa == "sim":
    sim +=1
else: 
    nao +=1

fantasia = input("Já se fantasiou de algum personagem?")

if fantasia == "sim":
    sim +=1
else: 
    nao +=1

action = input("Tem algum action figure/nave/etc?")

if action == "sim":
    sim +=1
else: 
    nao +=1

galaxy = input("Já foi no Galaxy's Edge, o parque temático da franquia?")

if galaxy == "sim":
    sim +=1
else: 
    nao +=1

if sim >=2 and sim <3:
    print("Padawan")
elif sim >=3 and sim <=4:
    print("Jedi")
elif sim ==5:
    print("One with the Force")
else: 
    print("Inocente")

