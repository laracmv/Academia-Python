# Escreva um programa que       pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso exiba a multa, cobrando R$5,00 por km acima de 80. (Ex. 4.2 livro Nilo Ney).

# A multa deve ser apresentada com exatamente duas casas decimais. Se o usuário não foi multado, imprima: 'Não foi multado'.

velocidade = float(input("Velocidade: "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Sua multa foi de: {multa: .2f}')
else: 
    print("Não foi multado")