"""
Libreria creada para realizar la practica #1, se hace libreria
nueva para tener un codigo mas limpio en el archivo principal
"""
import turtle
t = turtle.Turtle()

def teleport(x:float, y:float):
    """
    Funcion para mover el puntero sin dibujar
    """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def cuadro(lado_cara:float):
    """
    Funcion para dibujar un cuadro
    """
    t.setheading(0)
    for _ in range(4):
        t.forward(lado_cara)
        t.left(90)

def triangulo(lado_cara:float):
    """
    Funcion para dibujar un triangulo
    """
    t.setheading(0)
    for _ in range (2):
        t.forward(lado_cara)
        t.left(120)
    t.forward(lado_cara)

def circulo(radio:float):
    """
    Funcion para dibujar un circulo
    """
    t.setheading(0)
    pasos = 60
    avance = (2 * 3.14159 * radio) / pasos
    angulo = 360 / pasos
    for _ in range(pasos):
        t.forward(avance)
        t.left(angulo)

def linea(largo:int, angulo:float):
    """
    Funcion para dibujar una linea
    """
    turtle.speed(10)
    for _ in range(largo):
      t.left(angulo)
      t.forward(1)
      t.setheading(0)
