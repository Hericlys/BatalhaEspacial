import pygame
from pygame.locals import *
import os

pygame.init()
pygame.mixer.init()


class Configurações:
    def __init__(self, nome_do_jogo="Nave Game"):
        self.largura_tela = 32 * 30
        self.altura_tela = 32 * 22
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
        self.volume_musica = 0.1
        self.volume_efeitos = self.volume_musica + 0.2
        self.mudo = False


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

                if event.key == K_1:
                    nave_player.index_arma = 0

                if event.key == K_2:
                    nave_player.index_arma = 1

                if event.key == K_r:
                    nave_player.index_arma = 2

                if event.key == K_m:
                    if not config.mudo:
                        config.volume_musica = 0
                        config.volume_efeitos = 0
                        config.mudo = True
                    else:
                        config.volume_musica = 0.1
                        config.volume_efeitos = config.volume_musica + 0.2
                        config.mudo = False

                if event.key == K_UP:
                    if config.volume_musica < 0.5 and not config.mudo:
                        config.volume_musica += 0.1
                        config.volume_efeitos += 0.1
                if event.key == K_DOWN:
                    if config.volume_musica > 0 and not config.mudo:
                        config.volume_efeitos -= 0.1
                        config.volume_musica -= 0.1

                #botões para teste
                if event.key == K_0 and not nave_player.vida:
                    config.reiniciar()
                if event.key == K_9:
                    nave_player.pontos_de_vida -= 100

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

musica_fundo = pygame.mixer.music.load(os.path.join(SONS_DIR, "BoxCat Games - Battle (Special).mp3"))



sprite_sheet_nave = pygame.image.load(os.path.join(IMAGENS_DIR, "Nave_player.png"))
sprite_sheet_explosao = pygame.image.load(os.path.join(IMAGENS_DIR, "Explosão.png"))
sprite_sheet_disparos = pygame.image.load(os.path.join(IMAGENS_DIR, "Disparos.png"))

todas_as_sprites = pygame.sprite.Group()




