class BarraMana(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, tipojogador, tipooponente):
        # Construtor da classe mãe
        pygame.sprite.Sprite.__init__(self)

        self.tipojogador = tipojogador
        self.tipooponente = tipooponente
        self.image = assets['barra_mana']
        self.assets = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.centerx = x
        self.centery = y

        # mana - mana inicial
        self.mana = 0
        # taxamana - quantos pixels vai aumentar 
        self.taxamana = 1
        self.ultimo_mana = pygame.time.get_ticks()
        # ticks_mana - quantos milisegundos vai ter entre cada incremento
        self.ticks_mana = 100

    def drawbarra(self, superficie):
        larguramana = (475 * (self.mana / 100))
        superficie.blit(self.image, (self.centerx, self.centery))
        pygame.draw.rect(superficie, AZUL, (self.centerx + 13, self.centery + 10, larguramana, 30),border_radius = 8)

    def update(self):
        nowbarra = pygame.time.get_ticks()
        ticks_transcorridosbarra = nowbarra - self.ultimo_mana

        if ticks_transcorridosbarra > self.ticks_mana:
            # if para quando ocorre combos, acessa o dicionario de golpes e ve que bateu sem parar
            if Jogador.dicgolpes[f'jogador{self.tipojogador}'] > 3:
                print("funcionou")
                self.taxamana = 2
                self.ultimo_mana = nowbarra
                self.mana = min(self.mana + self.taxamana, 100)
            else:
                # if de uma barra de mana normal
                self.taxa = 1
                self.ultimo_mana = nowbarra
                # soma o valor da mana com a taxa, o limitando a 100 (largura maxima)
                self.mana = min(self.mana + self.taxamana, 100)