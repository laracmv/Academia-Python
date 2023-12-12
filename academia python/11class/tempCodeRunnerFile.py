class Carrinho:
    def __init__(self):
        dic = {}
        self.dic = dic
    
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dic:
            self.dic[nome_produto] = preco
        else:
            self.dic[nome_produto] += preco

    def total_do_produto(self, nome_produto):
        return self.dic[nome_produto]

c = Carrinho()
c.adiciona('banana', 5)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 5