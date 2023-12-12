def resolve_equacao_1o_grau(a,b):
    raiz= -b/a
    return raiz

a= int(input("Digite seu valor:"))
b= int(input("Digite seu valor:"))
raiz= resolve_equacao_1o_grau(a,b)

print(raiz)