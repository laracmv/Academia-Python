def estado(lista):
    i = 0
    maiorhora = 0
    maiorminuto = 0
    mairsegundo = 0
    maior = None
    while i < len(lista):
        l = lista[i]

        hora = int(l[11:13])
        minuto = int(l[14:16])
        segundo = int(l[17:19])

        if hora > maiorhora:
            maiorhora = hora
            maiorminuto = minuto
            maiorsegundo = segundo
            maior = l

            if minuto > maiorminuto:
                maiorhora = hora
                maiorminuto = minuto
                maiorsegundo = segundo
                maior = l
        
                if segundo > maiorsegundo:
                    maiorhora = hora
                    maiorminuto = minuto
                    maiorsegundo = segundo
                    maior = l
        
        i+=1
    maior = maior.lower()
    if "online" in maior:
        return 'ONLINE'
    else:
        return 'PARADO'

logs = [
    '2023-08-14 08:50:12 Falha código 467 - Sistema Online',
    '2023-08-14 13:50:12 Online',
    '2023-08-14 23:50:11 Sistema Parado após erro inexperado',
    '2023-08-14 23:12:45 Sistema reiniciado, está Online',
]

print(estado(logs))
