
resposta = None
qmin = 10
soma = 0
aprovados = 0
reprovados = 0
i = 0
media = 0

while resposta != 'não':
    resposta = input("Você quer adicionar mais alguma nota?")
    if resposta != "não":
        i+=1
        q1 = float(input("Nota quiz 1"))
        q2 = float(input("Nota quiz 2"))
        q3 = float(input("Nota quiz 3"))
        q4 = float(input("Nota quiz 4"))
        q5 = float(input("Nota quiz 5"))
        ai = float(input("Nota avaliação intermediária: "))
        af = float(input("Nota avaliação final: "))
        ep1 = float(input("Nota Ep1: "))
        ep2 = float(input("Nota Ep2: "))
        pf = float(input("Nota projeto final: "))

        if q1 < qmin:
            qmin = q1
        elif q2 < qmin:
            qmin = q2
        elif q3 < qmin:
            qmin = q3
        elif q4 < qmin:
            qmin = q4
        elif q5 < qmin:
            qmin = q5

        q = (q1 + q2 + q3 + q4 + q5 - qmin)/4
        ni = 0.4 * ai + 0.5 * af + 0.1 * q
        ng = 0.1 * ep1 + 0.2 * ep2 + 0.7 * pf
        if ni >=5 and ng >=5:
            nf = (ni + ng)/2
            aprovados +=1
        else: 
            reprovados +=1
            if ni < ng:
                nf = ni
            else:
                nf = ng

        print(f"Nota final do aluno: {nf:.2f}")
        soma += nf
    else:
        break

if i != 0:
    media = soma/i
if aprovados != 0:
    aprovados = (aprovados/i) * 100
if reprovados != 0:
    reprovados = (reprovados/i) * 100
print(f"Média da sala: {media:.2f}%")
print(f"Aprovados: {aprovados:.2f}%")
print(f"Reprovados: {reprovados:.2f}%")