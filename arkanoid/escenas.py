import pygame as pg
from . import FPS, ANCHO, ALTO
from .entidades import Raqueta, Bola, Ladrillo

class Escena():
    def __init__(self,pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        pass

class Portada(Escena):
    def __init__(self,pantalla):
        super().__init__(pantalla)
        #Escena.__init__(self, pantalla)
        self.logo = pg.image.load("resources/images/arkanoid_name.png")
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 45)
        self.callToAction = fuente.render("Pulsa <SPC> para comenzar", True, (0,0,0))
        #self.callToAction = pg.font.Font("resources/fonts/LibreFranklin-VariableFont_wght.ttf",24).render("Pulsa <SPC> para comenzar", False, (0,0,0))


    def bucle_principal(self):
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        game_over = True

            self.pantalla.fill((80,80,255))
            self.pantalla.blit(self.logo,(140,140))
            self.pantalla.blit(self.callToAction,((ANCHO - self.callToAction.get_width())//2, 620))

            pg.display.flip()


class Partida(Escena):
    def __init__(self,pantalla):
        super().__init__(pantalla)
        #self.vidas = 3
        self.fondo = pg.image.load("resources/images/background.jpg")
        self.entidades = pg.sprite.Group()
        self.player = Raqueta(midbottom=(ANCHO // 2, ALTO - 15) )
        self.bola = Bola(center=(ANCHO // 2, ALTO // 2) )

        self.puntos = 0

        #self.l1 = Ladrillo(30,10)
        #self.l2 = Ladrillo(120,10)
        #self.l3 = Ladrillo(210,10)
        #self.l4 = Ladrillo(300,10)
        #self.l5 = Ladrillo(390,10)
        #self.l5 = Ladrillo(480,10)

        self.ladrillos = pg.sprite.Group()
        for f in range(3):
            
            for c in range(6):
                ladrillo = Ladrillo(c*90+30, f * 30 + 10)
                self.ladrillos.add(ladrillo)

        self.entidades.add(self.ladrillos,self.player,self.bola)
        

    def bucle_principal(self):
        vidas = 3
        while vidas > 0:
            dt = self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True 
                    exit()       

            self.entidades.update(dt) 
            #self.bola.update(dt)

            self.bola.choque(self.player)

            tocados = pg.sprite.spritecollide(self.bola, self.ladrillos, True)
            if len(tocados) > 0:
                self.bola.velocidad_y *= -1
                self.puntos += len(tocados)*5
            '''
            for ladrillo in self.ladrillos:
                self.bola.choque(ladrillo)'''

            if not self.bola.viva:
                vidas -= 1
                self.bola.viva = True

             

            self.pantalla.blit(self.fondo,(0,0))
            self.entidades.draw(self.pantalla)
            '''self.pantalla.blit(self.player.image, self.player.rect)
            self.pantalla.blit(self.bola.image, self.bola.rect)

            for ladrillo in self.ladrillos:
                self.pantalla.blit(ladrillo.image, ladrillo.rect)'''

            pg.display.flip()


class Records(Escena):
    def __init__(self,pantalla):
        super().__init__(pantalla)
