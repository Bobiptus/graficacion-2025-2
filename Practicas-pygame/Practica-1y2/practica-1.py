import pygame

pygame.init()
pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 1 - Movimiento básico")

x, y = 300, 200
vel = 5
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
        
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]: # Verifica si se presiona Shift
        clock.tick(300)  # Aumenta la velocidad si se presiona Shift
    else:
        clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        if x - vel >= 0:  # Evita que el jugador salga de la pantalla por la izquierda
            x -= vel
    if teclas[pygame.K_RIGHT]:
        if x + vel <= 560:  # Evita que el jugador salga de la pantalla por la derecha
            x += vel
    if teclas[pygame.K_UP]:
        if y - vel >= 0:  # Evita que el jugador salga de la pantalla por arriba
            y -= vel
    if teclas[pygame.K_DOWN]:
        if y + vel <= 360:  # Evita que el jugador salga de la pantalla por abajo
            y += vel

    pantalla.fill((30, 30, 30))
    pygame.draw.rect(pantalla, (255, 0, 255), (x, y, 40, 40)) # Cambio de color
    pygame.display.update()

pygame.quit()