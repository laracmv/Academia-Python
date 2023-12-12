class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self, infesquerdo, supdireito):
        self.infesquerd = infesquerdo
        self.supdireito = supdireito
    
    def calcula_perimetro(self):
        base = abs(self.supdireito.x - self.infesquerd.x)
        altura = abs(self.supdireito.y - self.infesquerd.y)
        return 2 * (base + altura)

    def calcula_area(self):
        base = abs(self.supdireito.x - self.infesquerd.x)
        altura = abs(self.supdireito.y - self.infesquerd.y)
        return base * altura

ponto_inferior_esquerdo = Ponto(0, 0)
ponto_superior_direito = Ponto(4, 3)

ret = Retangulo(ponto_inferior_esquerdo, ponto_superior_direito)

perimetro = ret.calcula_perimetro()
print(perimetro)
        


