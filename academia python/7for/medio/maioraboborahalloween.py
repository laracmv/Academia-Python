def maior_abobora(especie,  lista):
    max = -1
    indice = -1
    if lista == []:
        return indice
    else:
        for fazendeiros in lista:
            for abobora in fazendeiros:
                if abobora[1] == especie:
                    if abobora[0] > max:
                        indice = lista.index(fazendeiros)
                        max = abobora[0]
                    elif abobora[0] == max:
                        indice = indice
    return indice

especie = "japonesa"
faz =[
  [[2.3, 'kabotia']],
  [[6.2, 'kabotia'], [5.5, 'moranga'], [2.5, 'japonesa'], [1.4, 'moranga']],
  [[4.2, 'moranga'], [9.2, 'moranga'], [14.2, 'moranga']],
  [[5.6, 'kabotia'], [16.2, 'kabotia']],
  [[5.5, 'japonesa'], [12.2, 'japonesa'], [12.3, 'japonesa']],
  [[1.2, 'moranga'], [9.2, 'japonesa'], [8.5, 'japonesa']],
]

print(maior_abobora(especie,faz))



