def verifica_preco(titulo, dicionario, tabela):
    tipo = dicionario[titulo]
    return tabela[tipo]

t = "Dom Quixote"
di = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cor = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
print(verifica_preco(t,di,cor))

