"""

"""

import turtle
import navi_tools

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#Se configura la pantalla
SCREEN = turtle.Screen()
SCREEN.title("Mi dibujo con Turtle")
SCREEN.bgcolor("white")
SCREEN.setup(width=600, height=600)

def main() -> None:
    filename = "dibujante.txt"
    with open(filename) as archivo:
        contenido = archivo.read()
    string_length = len(contenido)
    navi_tools.detectar(string_length, contenido)

main()
SCREEN.exitonclick()
