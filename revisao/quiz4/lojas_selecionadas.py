# Com o advento da Internet e a posterior expansão do e-commerce, tornou-se muito fácil realizar uma pesquisa online de preços de produtos e encontrar a loja com a melhor oferta. Sua tarefa será determinar, a partir de uma lista de compras, de qual loja cada produto deve ser encomendado.

# Faça uma função que recebe:

# um dicionário no qual as chaves são nomes de produtos e os valores são novos dicionários nos quais as chaves são nomes de lojas e os valores são os preço em cada loja;
# uma lista de produtos a serem comprados
# Sua função deve devolver um dicionário no qual as chaves são nomes de produtos e os valores são as lojas que os vendem pelo menor preço (apenas uma loja para cada produto). Você pode supor que, para um mesmo produto, todos os preços são distintos. Caso algum produto não conste no catálogo, no dicionário de retorno o valor associado à chave deve ser #!python 'nao consta'.

def lojas_selecionadas(dicionario, prodcomprar):
    dicinovo = {}
    for item in prodcomprar:
        if item not in dicionario:
            dicinovo[item] = "nao consta"
        else:
            minimo = None
            marcas = dicionario[item]
            for marca, valor in marcas.items():
                if minimo is None or valor < minimo:
                    minimo = valor
                    dicinovo[item] = marca

    return dicinovo

entrada =  {
    'fone de ouvido BT' : {
        'Americanas': 219.90,
        'Magazine Luiza': 209.90,
        'Amazon': 249.90      
    },
    'carregador celular USB-C': {
        'Mercado Livre': 50.00
    },
    'livro Programacao com Python': {
        'Magazine Luiza': 79.90,
        'Amazon': 59.90
    }                                           
}

compras = [
    'fone de ouvido BT',
]

print(lojas_selecionadas(entrada,compras))