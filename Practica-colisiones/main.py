import pygame
import random
pygame.init()

# Variables globales
SCORE = 0

pantalla = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 36)     # Agregue esta linea para establecer la fuente

jugador = pygame.Rect(50, 300, 40, 40)
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]
clock = pygame.time.Clock()
running = True

while running:
    pygame.display.set_caption("Practica - Colisiones")

    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600]

    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                SCORE += 1   # Esta línea incrementa el puntaje al colisionar
                balas.remove(b)
                enemigos.remove(e)
                x = random.randint(100, 360) # Aquí se genera una nueva posición x para el enemigo
                enemigos.append(pygame.Rect(x, 300, 40, 40)) # Aquí se agrega de nuevo el enemigo
                break
                
                
    pantalla.fill((0, 0, 0))
    text_surface = font.render(f"SCORE: {SCORE}", True, (255, 255, 255))  #Esta línea imprime el puntaje
    pantalla.blit(text_surface, (10, 10))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b)
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e)
    pygame.display.update()

pygame.quit()
