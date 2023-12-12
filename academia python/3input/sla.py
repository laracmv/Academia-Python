import math

# def f(mi,x):
#     exponencial=(-mi)*x
#     f=1-math.e**exponencial
#     return f

# mi = float(input("Qual a taxa (λ)? "))
# x = float(input("Qual x, para calcular F(λ, x)?"))
# f = f(mi,x)
# print(f"{f: .4f}")

mi = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)?"))
exponencial=(-mi)*x
f=1-math.e**exponencial
print(f"{f: .4f}")