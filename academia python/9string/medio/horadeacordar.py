def converteHora(horario):
    posicao = horario.find(":")
    priposicao = horario[:posicao]
    priposicao = int(priposicao)
    segposicao = horario[posicao:]
    if priposicao > 0 and priposicao >= 12:
        novohorario = str(priposicao - 12) + str(segposicao) + " PM"
        return novohorario
    else:
        novohorario = horario + " AM"
        return novohorario

print(converteHora("15:30"))
