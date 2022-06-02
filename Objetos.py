import pygame
import os
from Configurações import config, sprite_sheet_nave, sprite_sheet_explosao, sprite_sheet_disparos,SONS_DIR


class NavePlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vida = True
        self.pontos_de_vida = 100

        self.imagens_nave = []
        self.imagens_nave_explosao = []
        for i in range(6):
            img = sprite_sheet_nave.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 2, 32 * 2))
            img2 = sprite_sheet_explosao.subsurface((i * 32, 0), (32, 32))
            img2 = pygame.transform.scale(img2, (32 * 2, 32 * 2))
            self.imagens_nave.append(img)
            self.imagens_nave_explosao.append(img2)

        self.index_lista = 0
        self.index_lista_explosao = 0
        self.image = self.imagens_nave[self.index_lista]
        self.pos_x = config.largura_tela / 2
        self.pos_y = config.altura_tela - 32
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.minhasArmas = [Laser, LaserDuplo, Especial]
        self.index_arma = 0
        self.minhasBalas = []
        self.velocidade = 10
        self.son_explosao = pygame.mixer.Sound(os.path.join(SONS_DIR, "explosao_nave.wav"))

    def update(self):
        self.animaçao()
        self.movimentação()
        self.son_explosao.set_volume(config.volume_efeitos)

    def movimentação(self, direct_x=0, direct_y=0):
        if self.vida:
            self.pos_x += self.velocidade * direct_x
            self.pos_y += self.velocidade * direct_y
            self.rect.center = (self.pos_x, self.pos_y)

    def animaçao(self):
        if self.vida:
            if self.index_lista > 5:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_nave[int(self.index_lista)]

    def disparar(self):
        if self.vida:
            Arma = self.minhasArmas[self.index_arma]
            minha_bala = Arma(self.pos_x, self.pos_y)
            self.minhasBalas.append(minha_bala)

    def morte(self):
        self.vida = False
        if self.index_lista_explosao < 5:
            self.son_explosao.play()
            self.index_lista_explosao += 0.25
            self.image = self.imagens_nave_explosao[int(self.index_lista_explosao)]


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.son_disparoLaser = pygame.mixer.Sound(os.path.join(SONS_DIR, "DisparoLase.WAV"))
        self.son_disparoLaser.set_volume(config.volume_efeitos)
        self.son_disparoLaser.play()
        self.dano = 15
        self.pos_x = pos_x
        self.pos_y = pos_y - 32
        self.velocidade = 10
        self.image = sprite_sheet_disparos.subsurface((0, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.pos_y -= self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)


class LaserDuplo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.son_disparoLaser = pygame.mixer.Sound(os.path.join(SONS_DIR, "DisparoLase.WAV"))
        self.son_disparoLaser.set_volume(config.volume_efeitos)
        self.son_disparoLaser.play()
        self.dano = 25
        self.pos_x = pos_x
        self.pos_y = pos_y - 32
        self.velocidade = 15
        self.image = sprite_sheet_disparos.subsurface((1 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.pos_y -= self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)


class Especial(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.son_disparoLaser = pygame.mixer.Sound(os.path.join(SONS_DIR, "DisparoLase.WAV"))
        self.son_disparoLaser.set_volume(config.volume_efeitos)
        self.son_disparoLaser.play()
        self.dano = 100
        self.pos_x = pos_x
        self.pos_y = pos_y - 32
        self.velocidade = 15
        self.sprite_animacao = []
        self.index_lista = 0
        for i in range(2):
            img = sprite_sheet_disparos.subsurface(((i + 5) * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.sprite_animacao.append(img)
        self.image = self.sprite_animacao[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        if self.index_lista >= 1:
            self.index_lista = 0
        self.index_lista += 0.7
        self.image = self.sprite_animacao[int(self.index_lista)]
        self.pos_y -= self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)