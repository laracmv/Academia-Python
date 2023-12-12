def mais_populoso(dic):
    maior = 0
    soma = 0
    mestado = None
    for estado, municipios in dic.items():
        soma = 0
        for municipio, pop in municipios.items():
            soma += pop
        
        if soma > maior:
            maior = soma
            mestado = estado
    return mestado

brasil = {
    'Distrito Federal': {"Brasília": 3015268},
    "Bahia":{"Salvador": 2872347, "Feira de Santana":614872, "Vitória da Conquista": 341597},
    "Rio de Janeiro": {"Rio de Janeiro": 6718903, 'São Gonçalo': 1084839,"Duque de Caxias":919596},
    'Amazonas': {"Manaus": 2182763,"Parintins": 114273, "Itacoatiara":101337}
}

print(mais_populoso(brasil))

        


        