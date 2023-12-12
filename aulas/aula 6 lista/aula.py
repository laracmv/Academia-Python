# numeros que não podem realizar operacoes matematicas sao string. Exemplo: cpf pode começar com 0
nomes = [
    ["1humberto", "06729-52"],
    ["2humberto", ["9898107695", "9182182"], "06729-52"]
]

print(nomes[0][0])
# imprime valor dentro de lista
print(nomes[0][0][0])

alunos2 = nomes[1]
# fica mais facil se criar uma variavel
print(alunos2[1])

