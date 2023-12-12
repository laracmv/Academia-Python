# Vamos jogar?

# Faça uma função que recebe duas strings, correspondentes à escolha de cada jogador: "pedra","papel" ou "tesoura". A função deve devolver o jogador vencedor, sendo que este é reconhecido pela ordem dos argumentos fornecidos à função. Assim, o primeiro argumento se refere ao jogador "um" e o segundo ao jogador "dois".

# Por exemplo, caso os argumentos fornecidos sejam ("pedra", "papel"), a função deve retornar: "dois".

# Caso ocorra um empate, a função deve retornar a string "empate"

# Se a entrada for uma palavra diferente do esperado, a função deve devolver a mensagem: "Escolha pedra, papel ou tesoura para jogar"

# Você pode considerar que apenas duas pessoas jogarão por partida e que os argumentos fornecidos à função são sempre strings.

# O nome da sua função deve ser pedra_papel_tesoura


def pedra_papel_tesoura(j1, j2):
    if j1 == "pedra" and j2 == "tesoura":
        return "um"
    elif j1 == "papel" and j2 == "pedra":
        return "um"
    elif j1 == "tesoura" and j2 == "papel":
        return "um"
    elif j2 == "pedra" and j1 == "tesoura":
        return "dois"
    elif j2 == "papel" and j1 == "pedra":
        return "dois"
    elif j2 == "tesoura" and j1 == "papel":
        return "dois"
    elif j1 == j2 and j1 == "pedra":
        return "empate" 
    elif j1 ==j2  and j1 == "papel":
        return "empate"
    elif j1 == j2 and j1 == "tesoura":
        return "empate"  
    else:
        return "Escolha pedra, papel ou tesoura para jogar" 

print(pedra_papel_tesoura("tesouara", "papel"))