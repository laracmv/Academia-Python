# arredondar para baixo = math.floor
import math
def dias_de_racao(estoque, info):
    dias = 0
    if estoque == []:
        return dias
    else:
        for racoes in estoque:
            
            if info['porte'] == racoes['porte']:
                if info['idade'] <=1 and racoes['indicado'] == 'filhote':
                    quant = racoes['qtde']
                    diario = info['gramas_dia']
                    dias += (quant * 1000)/ diario
                if info['idade'] >1 and info['idade']<8 and racoes['indicado'] == 'adulto':
                    quant = racoes['qtde']
                    diario = info['gramas_dia']
                    dias += (quant * 1000)/ diario
                if info['idade'] >=8 and racoes['indicado'] == 'idoso':
                    quant = racoes['qtde']
                    diario = info['gramas_dia']
                    dias += (quant * 1000)/ diario
        return math.floor(dias)

estoque = [
  {
      'marca': 'premier',
      'porte': 'pequeno',
      'indicado': 'adulto',
      'qtde': 8
  },
  {
      'marca': 'royal c.',
      'porte': 'pequeno',
      'indicado': 'filhote',
      'qtde': 2.5
  }
]

teste = {
  'nome': 'totó',
  'idade': 0.9,
  'porte': 'pequeno',
  'gramas_dia': 200.0
}

print(dias_de_racao(estoque, teste))
                

