from random import choice
from Configurações import *
from player import NavePlayer
from inimigos import AlienVerde, AlienVermelho, AlienMarron
pygame.display.set_caption('Nave Game')
nave_player = NavePlayer()
todas_as_sprites.add(nave_player)

Lista_inimigos = []
todas_as_balas_dos_inimigos = []
pygame.mixer.music.play(-1)


if __name__ == "__main__":
    while True:
        config.relogio.tick(30)
        config.controle(nave_player)
        if nave_player.pontos_de_vida <= 0 or not nave_player.vida:
            nave_player.morte()
        todas_as_sprites.add(Lista_inimigos)

        if len(Lista_inimigos) < 1:
            tipo_inimigo = [AlienVerde, AlienVermelho, AlienMarron]
            tipo_inimigo = choice(tipo_inimigo)
            inimigo = tipo_inimigo(todas_as_balas_dos_inimigos)
            Lista_inimigos.append(inimigo)
        colisoes_ComInimigos = []
        for inimigo in Lista_inimigos:
            colisoes_ComInimigos = pygame.sprite.spritecollide(inimigo, Grupo_BalasNavePlayer, True, pygame.sprite.collide_mask)
            if colisoes_ComInimigos:
                inimigo.pontos_vida -= colisoes_ComInimigos[0].dano
                nave_player.minhasBalas = list(filter((colisoes_ComInimigos[0]).__ne__, nave_player.minhasBalas))
                if inimigo.pontos_vida <= 0:
                    config.pontos += inimigo.pontos
                    Lista_inimigos = list(filter((inimigo).__ne__, Lista_inimigos))
                    todas_as_sprites.remove(inimigo)

        print(f"{todas_as_sprites}")
        config.tela.fill((0, 0, 0))
        todas_as_sprites.add(todas_as_balas_dos_inimigos)
        todas_as_sprites.draw(config.tela)
        todas_as_sprites.update()
        pygame.display.flip()
        pygame.mixer.music.set_volume(config.volume_musica)
