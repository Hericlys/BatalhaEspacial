from Configurações import *
from player import NavePlayer
from inimigos import AlienVerde
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
            inimigo = AlienVerde(todas_as_balas_dos_inimigos)
            todos_os_inimigos.append(inimigo)

        config.tela.fill((0, 0, 0))
        todas_as_sprites.add(todas_as_balas_dos_inimigos)
        todas_as_sprites.draw(config.tela)
        todas_as_sprites.update()
        pygame.display.flip()
        pygame.mixer.music.set_volume(config.volume_musica)
        print(todas_as_balas_dos_inimigos)