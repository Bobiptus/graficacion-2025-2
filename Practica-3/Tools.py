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
    teleport (x,y)
    t.dot(2,color)

def revisa_color(codigo:int) -> str:
    paleta = ['white', 'black', 'green', 'red', 'yellow', 'purple', 'blue', 'cyan', 'chartreuse', 'deeppink']
    color_seleccionado = str(paleta[codigo])
    return color_seleccionado