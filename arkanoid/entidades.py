from arkanoid import ALTO, ANCHO
import pygame as pg
from pygame.sprite import Sprite

class Raqueta(Sprite):
    skin = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.skin}")
        self.rect = self.image.get_rect(**kwargs)

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5

        if pg.key.get_pressed()[pg.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x +=5


class Bola(Sprite):
    skin = "ball1.png"
    
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.skin}")
        self.rect = self.image.get_rect(**kwargs)
        self.velocidad_x = 5
        self.velocidad_y = 5
        self.viva = True
        self.posicion_inicial = kwargs

    def update(self):

        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad_x *= -1
        
        if self.rect.top <= 0:
            self.velocidad_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.rect = self.image.get_rect(**self.posicion_inicial)
        
            

    def choque(self,objeto):
        if self.rect.right >= objeto.rect.left and self.rect.left <= objeto.rect.right and self.rect.bottom >= objeto.rect.top and self.rect.top<= objeto.rect.bottom:
            self.velocidad_y *= -1




