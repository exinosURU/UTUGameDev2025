# Punto de entrada principal del juego.
# Inicializa Pygame, el motor y arranca el Game Loop con la escena inicial.


import pygame
from engine.config import ANCHO, ALTO
from engine.game_loop import GameLoop
from Elevator_Action.game import Juego

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Elevator Action")

    juego = Juego()
    game_loop = GameLoop(pantalla, juego)

    game_loop.run()
    pygame.quit()

if __name__ == "__main__":
    main()

