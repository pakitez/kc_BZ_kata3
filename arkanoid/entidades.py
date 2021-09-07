from arkanoid import ALTO, ANCHO, FPS
import pygame as pg
from pygame.sprite import Sprite

class Raqueta(Sprite):
    skin = ["electric00.png","electric01.png","electric02.png"]
    def __init__(self, **kwargs):
        super().__init__() #necesario introducir el init de sprite para poder generar group
        self.imagenes = []
        for archivo in self.skin:
            self.imagenes.append(pg.image.load(f"resources/images/{archivo}"))
        self.imagen_activa = 0

        self.tiempo_transcurrido = 0
        self.tiempo_cambio = 1000 // FPS * 5

        self.image = self.imagenes[self.imagen_activa]

        self.rect = self.image.get_rect(**kwargs)

    def update(self, dt):
        if pg.key.get_pressed()[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5

        if pg.key.get_pressed()[pg.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x +=5

        self.tiempo_transcurrido += dt
        if self.tiempo_transcurrido >= self.tiempo_cambio:
            self.imagen_activa += 1
            if self.imagen_activa >= len(self.imagenes):
                self.imagen_activa = 0
            
            self.tiempo_transcurrido = 0
        
        self.image = self.imagenes[self.imagen_activa]


class Bola(Sprite):
    skin = "ball1.png"
    
    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(f"resources/images/{self.skin}")
        self.rect = self.image.get_rect(**kwargs)
        self.velocidad_x = 5
        self.velocidad_y = 5
        self.viva = True
        self.posicion_inicial = kwargs

    def update(self, dt):

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad_x *= -1
        
        if self.rect.top <= 0:
            self.velocidad_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.reset()

    def reset(self):
        self.rect = self.image.get_rect(**self.posicion_inicial)
        self.velocidad_x = 5
        self.velocidad_y = 5
       

    def choque(self,objeto):
        if self.rect.right >= objeto.rect.left and self.rect.left <= objeto.rect.right and self.rect.bottom >= objeto.rect.top and self.rect.top <= objeto.rect.bottom:
            self.velocidad_y *= -1

class Ladrillo(Sprite):
    skin = "greenTile.png"
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(f"resources/images/{self.skin}")
        self.rect = self.image.get_rect(x=x, y=y)


    




