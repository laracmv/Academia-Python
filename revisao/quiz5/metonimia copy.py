def troca_nome(texto, dic):
    for marca, produto in dic.items():
        n = texto.lower().find(marca.lower())
        if n!= -1:
            antes = texto[:n]
            depois = texto[n + len(marca):]
            texto = antes + ("_" * len(produto)) + depois
    return texto    

tex = "Adicione uma colher de sopa de Maizena a dois copos de leite e leve ao fogo baixo, mexendo sempre. Ao final, acrescente o leite Moça."

metonimias = {
    'Leite Moça': 'leite condensado',
    'Leite Ninho': 'leite em pó',
    'Maizena': 'amido de milho',
}

print(troca_nome(tex, metonimias))
