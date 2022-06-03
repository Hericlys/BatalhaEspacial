from Configurações import *
from Objetos import NavePlayer, Alien1

pygame.display.set_caption('Nave Game')

nave_player = NavePlayer()
todas_as_sprites.add(nave_player)
alien = Alien1(100, 100)
todas_as_sprites.add(alien)
pygame.mixer.music.play(-1)


if __name__ == "__main__":
    while True:
        config.relogio.tick(30)

        config.controle(nave_player)
        if nave_player.pontos_de_vida <= 0 or not nave_player.vida:
            nave_player.morte()

        config.tela.fill((0, 0, 0))
        todas_as_sprites.draw(config.tela)
        todas_as_sprites.update()
        pygame.display.flip()
        pygame.mixer.music.set_volume(config.volume_musica)
