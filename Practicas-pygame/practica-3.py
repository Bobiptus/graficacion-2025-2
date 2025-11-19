import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

x, y = 50, 150   #Se cambio la posición del jugador para poder hacer disparos arriba y abajo
balas = []
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(200)  #Aqui se cambió la velocidad del disparo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                balas.append([pygame.Rect(x + 40, y + 15, 10, 5), 10, 0]) # Disparo horizontal
            if event.key == pygame.K_UP:
                balas.append([pygame.Rect(x + 40, y + 15, 10, 5), 10, -5])  # Disparo hacia arriba
            if event.key == pygame.K_DOWN:
                balas.append([pygame.Rect(x + 40, y + 15, 10, 5), 10, 5])   # Disparo hacia abajo

    for bala in balas:
        bala[0].x += bala[1]
        bala[0].y += bala[2]

    balas = [b for b in balas if b[0].x < 600 and 0 <= b[0].y <= 400]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))

    for bala in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), bala[0])
    
    pygame.display.update()

pygame.quit()
