# Normalização e seleção de dados é uma tarefa comum em quaisquer sistemas de processamento de informações. Faça uma função que recebe uma lista de palavras e um número de letras, então, a função deve retornar uma lista de palavras em minúsculas, com o número de letras informado e sem caracteres especiais no início e fim, sem repetições.

# Exemplo:
# O nome da sua função deve ser filtra

def filtra(listapalavra, numeroletras):
    listafiltro = []
    for palavra in listapalavra:
        if len(palavra) == numeroletras:
            menor = palavra.lower()
            if menor not in listafiltro:
                listafiltro.append(menor)
        
    return listafiltro


lista = ["LARA","lara", "laura"]
print(filtra(lista,4))