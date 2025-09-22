# Gestiona la entrada del jugador (teclado, mouse).
# Traduce teclas o clicks a acciones del juego (mover, saltar, disparar).

import pygame

class InputManager:
    def __init__(self):
        self.keys = pygame.key.get_pressed()

    def update(self):
        self.keys = pygame.key.get_pressed()

    def left(self) -> bool:
        return self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]

    def right(self) -> bool:
        return self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]



