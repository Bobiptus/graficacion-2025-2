import pygame
pygame.init()

# --- Configuración ---
ANCHO, ALTO = 1200, 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Direccional - Sprite Sheet")

fondo = pygame.image.load("Practica-5y6/background.png").convert()
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

VENTANA.blit(fondo, (0, 0))

#confiugurar el hadouken
hadouken = pygame.image.load("Practica-5y6/hadouken.png").convert_alpha()
hadouken = pygame.transform.scale(hadouken, (80, 30))

# --- Cargar Sprite Sheet ---
sprite_sheet = pygame.image.load("Practica-5y6/personaje_direcciones.png").convert_alpha()

FRAME_ANCHO = 230
FRAME_ALTO = 300
FILAS = 4
COLUMNAS = 4

# --- Función para extraer los cuadros de una fila ---
def obtener_frames(fila):
    frames = []
    for i in range(COLUMNAS):
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect)
        frames.append(frame)
    return frames

# --- Diccionario con las animaciones de cada dirección ---
animaciones = {
    "arriba": obtener_frames(3),
    "izquierda": obtener_frames(2),
    "abajo": obtener_frames(0),
    "derecha": obtener_frames(1)
}

# --- Variables de juego ---
x, y = ANCHO // 2, ALTO // 2
velocidad = 3
direccion = "abajo"
frame_index = 0
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # milisegundos entre cuadros
reloj = pygame.time.Clock()

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # --- Movimiento y dirección ---
    teclas = pygame.key.get_pressed()
    moviendo = False

    if teclas[pygame.K_UP]:
        if y > 0:
            y -= velocidad
            direccion = "arriba"
            moviendo = True
    elif teclas[pygame.K_DOWN]:
        if y < ALTO - FRAME_ALTO:
            y += velocidad
            direccion = "abajo"
            moviendo = True
    elif teclas[pygame.K_LEFT]:
        if x > 0:
            x -= velocidad
            direccion = "izquierda"
            moviendo = True
    elif teclas[pygame.K_RIGHT]:
        if x < ANCHO - FRAME_ANCHO:
            x += velocidad
            direccion = "derecha"
            moviendo = True
        #Aqui intente que saliera el hadouken al presionar escape, pero no logre que trabajara
    elif teclas[pygame.K_ESCAPE]:
        VENTANA.blit(hadouken, (x + FRAME_ANCHO // 2 - 40, y + FRAME_ALTO // 2 - 15))
        clock = pygame.time.Clock()
        clock.tick(60)
   
    # --- Actualizar animación ---
    ahora = pygame.time.get_ticks()
    if moviendo:
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
    else:
        direccion = "abajo" 
        frame_index = 1 

    # --- Dibujar ---
    VENTANA.fill((90, 150, 255))
    VENTANA.blit(fondo, (0, 0))
    VENTANA.blit(animaciones[direccion][frame_index], (x, y))
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()