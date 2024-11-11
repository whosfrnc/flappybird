import pygame

class Jogador:
    def __init__(self, tela, x, y):

        self.posicao = [x , y]
        self.tamanho = [32 , 32]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        self.contador = 0
        self.imagemAtual = 0
        self.tela = tela
        self.listaImagens = []

        for i in range(3):
            imagem = pygame.image.load(f'assets/passaro-{i}.png')

            imagem = pygame.transform.scale(imagem, self.tamanho)

            self.listaImagens.append(imagem)
        
        self.velocidadeAtual = 0
        self.gravidade = 1/60*10
        self.velocidadeMaxima = 1/60*100

    def desenhar(self):
        self.contador += 1
        if self.contador > 5:
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3

        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):
        self.velocidadeAtual = min(self.velocidadeAtual + self.gravidade, self.velocidadeMaxima)

        self.posicao = [self.posicao[0], self.posicao[1] + self.velocidadeAtual]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        self.teclas = pygame.key.get_pressed()
        if self.teclas[pygame.K_SPACE]:
            self.velocidadeAtual = -self.velocidadeMaxima*2

    
    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)