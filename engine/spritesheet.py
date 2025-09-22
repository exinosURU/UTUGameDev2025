# Maneja hojas de sprites (spritesheets).
# Permite cortar y extraer frames individuales para animaciones.
import json

import pygame, os

class Spritesheet:
    def __init__(self, ruta_imagen):
        self.sheet = pygame.image.load(ruta_imagen).convert_alpha()

    def ubicacion(self, rect):
        return self.sheet.subsurface(rect).copy()

    @staticmethod
    def carga_json(ruta_json, ruta_imagen):
        with open(ruta_json, "r") as archivo:
            datos = json.load(archivo)

        sheet = Spritesheet(ruta_imagen)
        lista_sprites = []

        for nombre, info in sorted(datos["frames"].items()):
            fr = info["frame"]
            rect = pygame.Rect(fr["x"], fr["y"], fr["w"], fr["h"])
            lista_sprites.append((sheet.ubicacion(rect)))

        return lista_sprites

