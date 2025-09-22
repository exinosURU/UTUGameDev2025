# Define el bucle principal del motor: actualización de lógica, entrada y renderizado.
# Controla el delta time (dt) para animaciones y movimientos fluidos.

import pygame
from .config import FPS

class GameLoop:
    def __init__(self, pantalla, escena):
        self.pantalla = pantalla
        self.escena = escena
        self.reloj = pygame.time.Clock()
        self.ejecutando = True

    def run(self):
        while self.ejecutando:
            dt = self.reloj.tick(FPS) / 1000.0

            #cerrar la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ejecutando = False

            # aca dibuja la escena
            self.escena.update(dt)
            self.escena.draw(self.pantalla)
            pygame.display.flip()

        pygame.quit()

