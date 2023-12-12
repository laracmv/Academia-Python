class Person:
    # init é sempre usada quando uma classe é inicializada
    def  __init__(self, name, age):
        self.name = name
        # self = guarda o objeto, usado para acessa-lo
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# __str__()
# Retorna algo quando o objeto é uma string
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

# metodos = funcoes que pertencem a uma classe 

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# deletar propriedades
del p1.name

# deletar objetos
del p1

# classes "vazias"
class Person:
    pass

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def envelhecer(self):
        self.idade += 1
        if self.idade >= 65:
            self.idade = 65

humberto = Pessoa('1berto', 27)
print(humberto.nome)
print(humberto.idade)

humberto.envelhecer()
print(humberto.idade)