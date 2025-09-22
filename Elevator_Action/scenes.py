# distintas escenas del juego: menú, nivel principal, game over, victoria.
# Cada escena tiene su propia lógica de actualización y renderizado.

import pygame
from engine.config import AZUL_OSCURO, ROJO
from engine.input_manager import InputManager

class ElevatorActionScene:
    def __init__(self):
        self.input = InputManager()

        #circulo
        self.x = 200
        self.y = 200
        self.radius = 25
        self.speed = 250  # píxeles/segundo

    def update(self, dt: float):
        self.input.update()

        if self.input.left():
            self.x -= self.speed * dt
        if self.input.right():
            self.x += self.speed * dt

    def draw(self, pantalla: pygame.Surface):
        pantalla.fill(AZUL_OSCURO)
        pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radius, 5)
