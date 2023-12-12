def formatar_tabela(letras):
    if not letras:
        return "Tabela vazia"

    num_colunas = len(letras[0])

    # Determine a largura máxima para cada coluna
    larguras = [max(len(linha[i]) for linha in letras) for i in range(num_colunas)]

    # Construa a linha superior da tabela
    linha_superior = "+-" + "-+-".join("-" * largura for largura in larguras) + "-+"

    # Inicialize a lista de linhas formatadas com a linha superior
    linhas_formatadas = [linha_superior]

    # Itere sobre as linhas de letras e as formate
    for linha in letras:
        linha_formatada = "| " + " | ".join(linha[i].ljust(largura) for i, largura in enumerate(larguras)) + " |"
        linhas_formatadas.append(linha_formatada)

    # Adicione a linha inferior à lista de linhas formatadas
    linhas_formatadas.append(linha_superior)

    # Junte as linhas formatadas em uma única string
    tabela_formatada = "\n".join(linhas_formatadas)

    return tabela_formatada

# Exemplo de uso:
tabela_de_letras = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

tabela_formatada = formatar_tabela(tabela_de_letras)
print(tabela_formatada)
