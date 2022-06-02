import pygame
from pygame.locals import *
import os


class Configurações:
    def __init__(self, nome_do_jogo="Nave Game"):
        self.largura_tela = 32 * 30
        self.altura_tela = 32 * 15
        self.tela_size = (self.largura_tela, self.altura_tela)
        self.metade_largura_tela = self.largura_tela / 2
        self.metade_altura_tela = self.altura_tela / 2
        self.limite_esquedo_tela = 0 + 32
        self.limite_direito_tela = self.largura_tela - 32
        self.limite_superior_tela = 0 + 32
        self.limite_inferior_tela = self.altura_tela - 32
        self.tela = pygame.display.set_mode(self.tela_size)
        pygame.display.set_caption(nome_do_jogo)
        self.relogio = pygame.time.Clock()

    def reiniciar(self):
        print("funciona")

    def controle(self, nave_player):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    nave_player.disparar()
                    todas_as_sprites.add(nave_player.minhasBalas)
                if event.key == K_0 and nave_player.vida == False:
                    config.reiniciar()
                if event.key == K_9:
                    nave_player.pontos_de_vida -= 50

        if pygame.key.get_pressed()[pygame.K_a]:
            if nave_player.pos_x > self.limite_esquedo_tela:
                nave_player.movimentação(-1, 0)
        if pygame.key.get_pressed()[pygame.K_d]:
            if nave_player.pos_x < self.limite_direito_tela:
                nave_player.movimentação(1, 0)
        if pygame.key.get_pressed()[pygame.K_w]:
            if nave_player.pos_y > self.metade_altura_tela:
                nave_player.movimentação(0, -1)
        if pygame.key.get_pressed()[pygame.K_s]:
            if nave_player.pos_y < self.limite_inferior_tela:
                nave_player.movimentação(0, 1)


config = Configurações()
BASE_DIR = os.path.dirname(__file__)
IMAGENS_DIR = os.path.join(BASE_DIR, "IMAGENS")
SONS_DIR = os.path.join(BASE_DIR, "SONS")

sprite_sheet_nave = pygame.image.load(os.path.join(IMAGENS_DIR, "Nave_player.png"))
sprite_sheet_explosao = pygame.image.load(os.path.join(IMAGENS_DIR, "Explosão.png"))
sprite_sheet_disparos = pygame.image.load(os.path.join(IMAGENS_DIR, "Disparos.png"))

todas_as_sprites = pygame.sprite.Group()


