from random import choice

import pygame.sprite

from Configurações import *
from player import NavePlayer
from inimigos import AlienVerde, AlienVermelho, AlienMarron
pygame.display.set_caption('Nave Game')
nave_player = NavePlayer()
todas_as_sprites.add(nave_player)

todos_os_inimigos = []
todas_as_balas_dos_inimigos = []
pygame.mixer.music.play(-1)


if __name__ == "__main__":
    while True:
        config.relogio.tick(30)
        config.controle(nave_player)
        if nave_player.pontos_de_vida <= 0 or not nave_player.vida:
            nave_player.morte()
        todas_as_sprites.add(todos_os_inimigos)

        if len(todos_os_inimigos) < 1:
            tipo_inimigo = [AlienVerde, AlienVermelho, AlienMarron]
            tipo_inimigo = choice(tipo_inimigo)
            tipo_inimigo = AlienVerde
            inimigo = tipo_inimigo(todas_as_balas_dos_inimigos)
            todos_os_inimigos.append(inimigo)
        colisoes = []
        for inimigo in todos_os_inimigos:
            colisoes = pygame.sprite.spritecollide(inimigo, Grupo_inimigos, False, pygame.sprite.collide_mask)
        if colisoes:
            for inimigo in colisoes:
                print("bateu")
                del(inimigo)

        config.tela.fill((0, 0, 0))
        todas_as_sprites.add(todas_as_balas_dos_inimigos)
        todas_as_sprites.draw(config.tela)
        todas_as_sprites.update()
        pygame.display.flip()
        pygame.mixer.music.set_volume(config.volume_musica)
