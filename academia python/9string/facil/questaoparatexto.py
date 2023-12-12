def questao_para_texto(dicionario, id):
    resul = "----------------------------------------\n"
    resul += f"QUESTAO {id}\n\n"
    resul += f"{dicionario['titulo']}\n\n"
    resul += "RESPOSTAS:"
    for letra , pergunta in dicionario['opcoes'].items():
        resul += f"\n{letra}: {pergunta}"
    return resul


d = {
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}
id = 5
print(questao_para_texto(d, id))