"""
Cargar un archivo que contenga solo numeros del 0-9 "almenos que quieran mas colores",
asignarle un color a cada numero y cargar el archivo con la matriz de 100x100.

Usando turtle, y el valor leido de la matriz mover la tortuga a la coordenada
correspondiente y pintar el pixel del color asignado.

Asegúrate de que la matriz tenga variedad de colores para ser identificados.

Lista de colores:
    0) Blanco
    1) Negro
    2) Verde
    3) Rojo
    4) Amarillo
    5) Purpura
    6) Azul
    7) Cyan
    8) Monasterio
    9) Roja profundo

"""
import turtle
import Tools

COORDENADA_X = 0
COORDENADA_Y = 0

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#Se configura la pantalla
SCREEN = turtle.Screen()
SCREEN.title("Mi dibujo con Turtle")
SCREEN.bgcolor("white")
SCREEN.setup(width=600, height=600)

def main():
    """
    Funcion principal que lee el archivo y lo convierte en una cadena para su análisis
    """
    contador_pixeles = 0
    global COORDENADA_X, COORDENADA_Y
    filename = "imagen.txt"
    for line in open(filename):
        seq = line.split()
        if seq:  #Esta condición revisa si aún hay caracteres en el archivo
            for w in seq[0]: #Esta condición es para saber si no hemos terminado la cadena
                if w and int(w) != 0: #Esta condición es para no imprimir en color blanco
                    color_pixel = Tools.revisa_color(int(w))
                    Tools.print_dot(COORDENADA_X, COORDENADA_Y, color_pixel)
                COORDENADA_X = COORDENADA_X + 1
                contador_pixeles = contador_pixeles + 1
                if contador_pixeles == 100: #Condición para brincar de renglón
                    contador_pixeles = 0
                    COORDENADA_X = 0
                    COORDENADA_Y = COORDENADA_Y - 1
        else:
            return

COORDENADA_X = -100
COORDENADA_Y = 100

main()

SCREEN.exitonclick()
