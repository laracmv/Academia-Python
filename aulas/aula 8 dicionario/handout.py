#basico

idade = {"keys": 18, "chaves": 20}
#keys e value = item
print(idade["keys"])

#pode-se criar dicionarios vazios

idade = {}
vazio = dict()

#para adicionar novo item nele não precisar appendar

meu_dicionario = {}
meu_dicionario['vida universo e tudo mais'] = 42
print(meu_dicionario)

#verificar se valor existe no dicionario use in

port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}

port = 'alface'

if port in port2eng:
    eng = port2eng[port]
    print('{0} em inglês é {1}'.format(port, eng))
else:
    print('A palavra {0} não existe no dicionário'.format(port))

#mostrar chaves / keys

print(port2eng.keys())

#mostrar valores / values

print(port2eng.values())

#mostrar itens

print(dicionario.items())

#deletar

port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}
del port2eng['repolho']

#dicionario possiveis

di = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}

for i in di:
    print(i)

for i in di.values():
    print(i)

#percorrer dicionario

for key, value in dicionario.item():
    print(f"O {key} é {value}")

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf']= input('teste')
    estado['sigla'] = input('teste')
    brasil.append(estado.copy())

print(brasil)



