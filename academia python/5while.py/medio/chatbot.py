n = "i"

while n!="encerrar" and n!= "tchau":
    n = input("Digite algo: ")
    if n == "oi":
        print("Olá!")
    elif n == "bom dia":
        print("Bom dia")
    elif n == "site":
        print("Acesse https://insper.edu.br")
    elif n == "blackboard":
        print("Lá temos materiais, notas e muito mais!")
    elif n == "tchau":
        print("Até logo")
    elif n == "encerrar":
        print("Até logo")
    else:
        print("Não sei como te ajudar!")