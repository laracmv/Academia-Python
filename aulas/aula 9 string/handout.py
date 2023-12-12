#contar ocorrencias
print("banana".count("a"))

#somar strings:
print("abcd" + "efg")

#metodos
#retornar primeira ocorrencia de string, caso nao tenha retorna -1
print("abcd carro".find("carro"))

#trocar strings
print('abcba'.replace('b', 'd'))
#posso por a primeira aparicao de determinado numero, assiM;
print("abcdba".replace("b", "d", 1))

#remover carac em branco:
'   uma frase  \n'.strip()
# quando o termo é especificado remove o primeiro caracter do final ate um que nao seja especificado
print("testeeee".rstrip("e"))

#pegar string c virugla e criar uma lista, onde cada elemento é um indice. Se nao tiver virgula cada espaço entre palavras formará novo indice.
novo = 'uma palavra outra palavra última palavra'
print(novo.split(' '))
print()

'palavras separadas por espaço'.split() 

#pegar lista, devolver string:
print('() '.join(['a', 'b', 'c']))
print(' '.join(['a', 'b', 'c']))

s = "Engenharia Insper"
pos = s.find("Ins")
print(pos)
t = s.replace("Ins", "Su")
print(t)

#Fateamento - pegar partes especificas de string
s = "Insper"
t = s[2:4]
print(t)
#pega o primeiro mas nao o ultimo
# pode-se fazer assim:
[:2] 
#desde o inicio
[2:]
#ate o final
[:]
#inicio ao final
[1:1:1]
#o ultimo diz de quanto em quanto pula

# -1 pega o ultimo elemento
s = "Engenharia"
print(s[-1])

s1 = "Insper"
print(s1[::-2])

#

nome = "Lara"
nome.center(100)
print(nome)