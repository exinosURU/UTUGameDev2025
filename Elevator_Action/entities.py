# entidades del juego (jugador, enemigos, ascensores, ítems).
# Cada entidad hereda de GameObject o PhysicsObject.

import pygame, os
from pathlib import Path
from engine.spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, posicion=(100,100)):
        super().__init__()

        #Raiz del proyecto
        RAIZ = Path(__file__).resolve().parents[1] # <-- El índice 1 es porque hay que subir 2 niveles para llegar a la raiz

        carpeta = RAIZ / "assets" / "sprites" / "Player" / "idle"

        #Cargar los frames desde el json
        self.frames = Spritesheet.carga_json(
            os.path.join(carpeta, "Player_idle.json"),
            os.path.join(carpeta, "Player_idle.png")
        )


        # Cargo el sprite 3
        self.image = self.frames[2]
        self.rect = self.image.get_rect(topleft=posicion)
