# distintas escenas del juego: menú, nivel principal, game over, victoria.
# Cada escena tiene su propia lógica de actualización y renderizado.

import pygame
from engine.config import AZUL_OSCURO, ROJO
from engine.input_manager import InputManager
from Elevator_Action.entities import Player

class ElevatorActionScene:
    def __init__(self):
        self.input = InputManager()

        #Todos los sprites de la escena así se actualizan juntos
        self.todos = pygame.sprite.Group()
        self.player = Player(posicion=(200, 200))
        self.todos.add(self.player)
        self.speed = 250


        #circulo
        #self.x = 200
        #self.y = 200
        #self.radius = 25
        #self.speed = 250  # píxeles/segundo

    def update(self, dt: float):
        self.input.update()

        # Movimiento del jugador
        if self.input.left():
            self.player.rect.x -= self.speed * dt
            #self.x -= self.speed * dt  <- esto era del círculo
        if self.input.right():
            self.player.rect.x += self.speed * dt
            #self.x += self.speed * dt   <- esto era del círculo

        # Limites de la pantalla para el jugador
        area = pygame.display.get_surface()
        if area:
            ancho, alto = area.get_size()
            self.player.rect.x = max(0, min(self.player.rect.x, ancho - self.player.rect.width))
            self.player.rect.y = max(0, min(self.player.rect.y, alto - self.player.rect.height))


        self.todos.update(dt)

    def draw(self, pantalla: pygame.Surface):
        pantalla.fill(AZUL_OSCURO)
        #pygame.draw.circle(pantalla, ROJO, (self.x, self.y), self.radius, 5) # <- esto era del círculo
        self.todos.draw(pantalla)
