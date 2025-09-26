import turtle
t = turtle.Turtle()
t.speed(0)

def teleport(x:float, y:float) -> None:
    """
    Funcion para mover el puntero sin dibujar
    """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def print_dot(x:float, y:float, color:str) -> None:
    """
    Funcion para pintar un pixel en las coordenadas indicadas
    """
    teleport (x,y)
    t.dot(2,color)

def revisa_color(codigo:int) -> str:
    """"
    Funcion que se utiliza cuando se desigan el color, este es indicado por el numero que aparece en el arreglo, las opciones son las siguientes:

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
    paleta = ['white', 'black', 'green', 'red', 'yellow', 'purple', 'blue', 'cyan', 'chartreuse', 'deeppink']
    color_seleccionado = str(paleta[codigo])
    return color_seleccionado