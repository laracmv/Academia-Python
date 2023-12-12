import random

def sorteia_questao_inedita(dic, nivel, ljasorteada):
    nivelquestao = dic[nivel]
    sorteada = random.choice(nivelquestao)
    while sorteada in ljasorteada:
        if sorteada in ljasorteada:
            sorteada = random.choice(nivelquestao)
        else:
            ljasorteada.append(sorteada)
            return sorteada
    ljasorteada.append(sorteada)
    return sorteada, ljasorteada

entrada = {
"facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
}
  

sort = [
  {
    "titulo": "Qual destes parques não se localiza em São Paulo?!",
    "nivel": "facil",
    "opcoes": {
      "A": "Ibirapuera",
      "B": "Parque do Carmo",
      "C": "Parque Villa Lobos",
      "D": "Morro da Urca"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual o resultado da operação 57 + 32?",
    "nivel": "facil",
    "opcoes": {
      "A": "-19",
      "B": "85",
      "C": "89",
      "D": "99"
    },
    "correta": "C"
  },
  {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    }
]

print(sorteia_questao_inedita(entrada, "facil",sort ))
