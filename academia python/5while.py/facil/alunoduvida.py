# Faça um programa que pergunta ao aluno se ele tem dúvidas na disciplina. Se o aluno responder qualquer coisa diferente de "não", escreva "Pratique mais" e pergunte novamente se ele tem dúvidas. Continue perguntando até que o aluno responda que não tem dúvidas. Finalmente, escreva "Até a próxima".

# Seu programa deve imprimir as strings exatamente como descritas acima e nada mais.

duvidas = True

while duvidas == True:
    duvidas = input("Você tem duvidas?")
    if duvidas == 'não':
        duvidas = False
        print("Até a próxima")
    
    else: 
        print("Pratique mais")
        duvidas = True 