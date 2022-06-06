import os.path
import pygame.mixer
from Configurações import *
from random import randint, randrange, choice


class AlienVerde(pygame.sprite.Sprite):
    def __init__(self, todas_as_balas=[]):
        pygame.sprite.Sprite.__init__(self)
        self.velocidades = [1, 2, 3, 4, 5]
        self.velocidade = choice(self.velocidades)
        self.pos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.pos_y = randrange(config.limite_superior_tela, config.metade_altura_tela)
        self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)
        self.index_lista = 0
        self.imagens_alien = []
        for i in range(2):
            image = sprite_sheet_alien.subsurface((i * 32, 0), (32, 32))
            image = pygame.transform.scale(image, (32 * 1.5, 32 * 1.5))
            self.imagens_alien.append(image)
        self.image = self.imagens_alien[self.index_lista]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (self.pos_x, self.pos_y)
        self.som_disparo = pygame.mixer.Sound(os.path.join(SONS_DIR, 'tiro-inimigo-verde.wav'))
        self.som_disparo.set_volume(config.volume_efeitos)
        self.balas = todas_as_balas

    def update(self):
        self.animação()
        self.movimentação_x()
        self.movimentação_y()
        self.disparo()
        self.som_disparo.set_volume(config.volume_efeitos)

    def animação(self):
        if self.index_lista >= 1:
            self.index_lista = 0
        self.index_lista += 0.05
        self.image = self.imagens_alien[int(self.index_lista)]

    def movimentação_x(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_x % self.velocidade != 0:
            self.pos_x += 1
        if self.pos_x != self.novapos_x and self.novapos_x % self.velocidade == 0:
            if self.pos_x > self.novapos_x:
                self.pos_x -= self.velocidade
            else:
                self.pos_x += self.velocidade
        if self.pos_x == self.novapos_x or self.novapos_x % self.velocidade != 0:
            self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)

    def movimentação_y(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_y % self.velocidade != 0:
            self.pos_y += 1
        if self.pos_y != self.novapos_y and self.novapos_y % self.velocidade == 0:
            if self.pos_y > self.novapos_y:
                self.pos_y -= self.velocidade
            else:
                self.pos_y += self.velocidade
        if self.pos_y == self.novapos_y or self.novapos_y % self.velocidade != 0:
            self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela  / 2)

    def disparo(self):
        disparo = randint(0, 250)
        if disparo == 1:
            bala = ArmaAlenVerde(self.pos_x, self.pos_y)
            self.balas.append(bala)
            Grupo_inimigos.add(bala)
            self.som_disparo.play()
        if self.balas:
            if self.balas[0].pos_y > config.limite_inferior_tela:
                del(self.balas[0])


class ArmaAlenVerde(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade = 2
        self.direcao = 1
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_d = pos_x + 32
        self.move_e = pos_x - 32
        self.image = sprite_sheet_disparos.subsurface((2*32, 0), (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.movimento()

    def movimento(self):
        if self.pos_x == self.move_d:
            self.direcao = -1
        if self.pos_x == self.move_e:
            self.direcao = 1
        self.pos_x += self.velocidade * self.direcao
        self.pos_y += self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)


class AlienVermelho(pygame.sprite.Sprite):
    def __init__(self, todas_as_balas=[]):
        pygame.sprite.Sprite.__init__(self)
        self.velocidades = [5, 6, 7]
        self.velocidade = choice(self.velocidades)
        self.pos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.pos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)
        self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)
        self.index_lista = 0
        self.imagens_alien = []
        for i in range(2):
            image = sprite_sheet_alien.subsurface(((i+2) * 32, 0), (32, 32))
            image = pygame.transform.scale(image, (32 * 1.5, 32 * 1.5))
            self.imagens_alien.append(image)
        self.image = self.imagens_alien[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.som_disparo = pygame.mixer.Sound(os.path.join(SONS_DIR, 'tiro-inimigo-vermelho.wav'))
        self.som_disparo.set_volume(config.volume_efeitos)
        self.balas = todas_as_balas

    def update(self):
        self.animação()
        self.movimentação_x()
        self.movimentação_y()
        self.disparo()
        self.som_disparo.set_volume(config.volume_efeitos)

    def animação(self):
        if self.index_lista >= 1:
            self.index_lista = 0
        self.index_lista += 0.05
        self.image = self.imagens_alien[int(self.index_lista)]

    def movimentação_x(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_x % self.velocidade != 0:
            self.pos_x += 1
        if self.pos_x != self.novapos_x and self.novapos_x % self.velocidade == 0:
            if self.pos_x > self.novapos_x:
                self.pos_x -= self.velocidade
            else:
                self.pos_x += self.velocidade
        if self.pos_x == self.novapos_x or self.novapos_x % self.velocidade != 0:
            self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)

    def movimentação_y(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_y % self.velocidade != 0:
            self.pos_y += 1
        if self.pos_y != self.novapos_y and self.novapos_y % self.velocidade == 0:
            if self.pos_y > self.novapos_y:
                self.pos_y -= self.velocidade
            else:
                self.pos_y += self.velocidade
        if self.pos_y == self.novapos_y or self.novapos_y % self.velocidade != 0:
            self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)

    def disparo(self):
        disparo = randint(0, 300)
        if disparo == 1:
            bala = ArmaAlenVermelho(self.pos_x, self.pos_y)
            self.balas.append(bala)
            self.som_disparo.play()
        if self.balas:
            if self.balas[0].pos_y > config.limite_inferior_tela:
                del(self.balas[0])


class ArmaAlenVermelho(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade = 10
        self.direcao = 1
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_d = pos_x + 32
        self.move_e = pos_x - 32
        self.image = sprite_sheet_disparos.subsurface((4*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.movimento()

    def movimento(self):
        self.pos_y += self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)


class AlienMarron(pygame.sprite.Sprite):
    def __init__(self, todas_as_balas=[]):
        pygame.sprite.Sprite.__init__(self)
        self.velocidades = [8, 9, 10]
        self.velocidade = choice(self.velocidades)
        self.pos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.pos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)
        self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)
        self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)
        self.index_lista = 0
        self.imagens_alien = []
        for i in range(2):
            image = sprite_sheet_alien.subsurface(((i+4) * 32, 0), (32, 32))
            image = pygame.transform.scale(image, (32 * 1.5, 32 * 1.5))
            self.imagens_alien.append(image)
        self.image = self.imagens_alien[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.som_disparo = pygame.mixer.Sound(os.path.join(SONS_DIR, 'tiro-inimigo-de-fogo.wav'))
        self.som_disparo.set_volume(config.volume_efeitos)
        self.balas = todas_as_balas

    def update(self):
        self.animação()
        self.movimentação_x()
        self.movimentação_y()
        self.disparo()
        self.som_disparo.set_volume(config.volume_efeitos)

    def animação(self):
        if self.index_lista >= 1:
            self.index_lista = 0
        self.index_lista += 0.05
        self.image = self.imagens_alien[int(self.index_lista)]

    def movimentação_x(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_x % self.velocidade != 0:
            self.pos_x += 1
        if self.pos_x != self.novapos_x and self.novapos_x % self.velocidade == 0:
            if self.pos_x > self.novapos_x:
                self.pos_x -= self.velocidade
            else:
                self.pos_x += self.velocidade
        if self.pos_x == self.novapos_x or self.novapos_x % self.velocidade != 0:
            self.novapos_x = randrange(config.limite_esquedo_tela, config.limite_direito_tela)

    def movimentação_y(self):
        self.rect.center = (self.pos_x, self.pos_y)
        if self.pos_y % self.velocidade != 0:
            self.pos_y += 1
        if self.pos_y != self.novapos_y and self.novapos_y % self.velocidade == 0:
            if self.pos_y > self.novapos_y:
                self.pos_y -= self.velocidade
            else:
                self.pos_y += self.velocidade
        if self.pos_y == self.novapos_y or self.novapos_y % self.velocidade != 0:
            self.novapos_y = randrange(config.limite_superior_tela, config.metade_altura_tela / 2)

    def disparo(self):
        disparo = randint(0, 300)
        if disparo == 1:
            bala = ArmaAlenMarron(self.pos_x, self.pos_y)
            self.balas.append(bala)
            self.som_disparo.play()
        if self.balas:
            if self.balas[0].pos_y > config.limite_inferior_tela:
                del(self.balas[0])


class ArmaAlenMarron(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade = 20
        self.direcao = 1
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.move_d = pos_x + 32
        self.move_e = pos_x - 32
        self.image = sprite_sheet_disparos.subsurface((3*32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def update(self):
        self.movimento()

    def movimento(self):
        self.pos_y += self.velocidade
        self.rect.center = (self.pos_x, self.pos_y)