import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

x, y = 300, 300
vel_y = 0
gravedad = .5 # Se cambio la gravedad del salgo
en_suelo = True
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y += vel_y
    vel_y += gravedad

    if y >= 300:
        y = 300
        vel_y = 0
        en_suelo = True

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.draw.line(pantalla, (255, 255, 255), (0, 340), (600, 340), 5) # Se pinta el suelo
    pygame.display.update()

pygame.quit()