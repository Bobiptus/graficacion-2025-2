import pygame
import random
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 5 - Sprites y fondo")
fuente = pygame.font.Font(None, 36)

SPRITES = [
    pygame.transform.scale(pygame.image.load("Practica-5y6/fondo.png"), (1200,400)),
    pygame.transform.scale(pygame.image.load("Practica-5y6/walking_right.png"), (40,40)),
    pygame.transform.scale(pygame.image.load("Practica-5y6/walking_left.png"), (40,40)),
    pygame.transform.scale(pygame.image.load("Practica-5y6/flying_left.png"), (40,40)),
    pygame.transform.scale(pygame.image.load("Practica-5y6/flying_right.png"), (40,40))
]

class Pelota:
    def __init__(self, x, y, color, radio):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.existe = True

    #Funciones para la pelota
    def dibujar(self, pantalla):
        if self.existe:
            pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)

    def colision_disparo(self, disparos):
        for disparo in disparos:
            # Verificar si el disparo toca la pelota
            distancia = ((disparo[0] - self.x)**2 + (disparo[1] - self.y)**2)**0.5
            if distancia < self.radio:
                self.existe = False
                disparos.remove(disparo)
                return True
        return False

# Variables iniciales
LAST_KEY = "RIGHT"
DIRECCION = SPRITES[1]
x = 0
piso_albatros = 360
clock = pygame.time.Clock()
running = True
jumping = False
jumping_velocity = 0
GRAVEDAD = 0.5
JUMP_STRENGTH = -10
PISO = 360
disparos = []
score = 0

pelota = Pelota(random.randint(0, 600), random.randint(300, 320), (255, 0, 0), 15)
# Bucle principal
while running:
    if LAST_KEY == "RIGHT" and not jumping:
        DIRECCION = SPRITES[1]
    elif LAST_KEY == "LEFT" and not jumping:
        DIRECCION = SPRITES[2]

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                DIRECCION = SPRITES[1]
                LAST_KEY = "RIGHT"
                if x > -600:
                    x -= 10
            if event.key == pygame.K_LEFT:
                DIRECCION = SPRITES[2]
                LAST_KEY = "LEFT"
                if x < 0:
                    x += 10
            if event.key == pygame.K_SPACE:
                if LAST_KEY == "RIGHT":
                    disparos.append([300 + 40, piso_albatros + 15, "RIGHT"])
                else:
                    disparos.append([300 - 10, piso_albatros + 15, "LEFT"])
            if event.key == pygame.K_UP:
                if not jumping:
                    jumping = True
                    jumping_velocity = JUMP_STRENGTH
                    if LAST_KEY == "RIGHT":
                        DIRECCION = SPRITES[4]
                    else:
                        DIRECCION = SPRITES[3]
    if jumping:
        piso_albatros += jumping_velocity
        jumping_velocity += GRAVEDAD
        if piso_albatros >= PISO:
            jumping = False
            piso_albatros = PISO
            jumping_velocity = 0
            if LAST_KEY == "RIGHT":
                DIRECCION = SPRITES[4]
            else:
                DIRECCION = SPRITES[3]
                
    for disparo in disparos:
        if disparo[2] == "RIGHT":
            disparo[0] += 15
        else:
            disparo[0] -= 15
    
    disparos = [d for d in disparos if 0 <= d[0] <= 600]

    if pelota.existe:
        pelota.colision_disparo(disparos)
    else:
        score += 1
        pelota = Pelota(random.randint(0, 600), random.randint(300, 320), (255, 0, 0), 15)

    pantalla.blit(SPRITES[0], (x, 0))
    pantalla.blit(DIRECCION, (300, piso_albatros))

    pelota.dibujar(pantalla)
    
    for disparo in disparos:
        if disparo[2] == "RIGHT":
            pygame.draw.rect(pantalla, (0, 0, 255), (disparo[0], disparo[1], 10, 5))
        else:
            pygame.draw.rect(pantalla, (0, 0, 255), (disparo[0], disparo[1], 10, 5))
    
    texto_puntuacion = fuente.render(f"Puntuación: {score}", True, (0, 0, 0))
    pantalla.blit(texto_puntuacion, (10, 10))
    pygame.display.update()
    

pygame.quit()
