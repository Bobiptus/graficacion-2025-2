"""
Módulo Navi: Manejo de la navegación y dibujo de figuras con turtle graphics.
"""
import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
COORDENADA_X , COORDENADA_Y = 0, 0
FIGURA_GLOBAL = ""

def teleport_1t(coordenada_x:float, coordenada_y:float) -> None:
    """
    Funcion para mover el puntero sin dibujar
    """
    t.penup()
    t.setx(coordenada_x)
    t.sety(coordenada_y)
    t.pendown()

def teleport_2t(coordenada_x:float, coordenada_y:float) -> None:
    """
    Funcion para mover el puntero sin dibujar
    """
    t2.penup()
    t2.setx(coordenada_x)
    t2.sety(coordenada_y)
    t2.setheading(0)
    t2.pendown()

def draw_something(lado) -> None:
    """
    Función para dibujar una figura geométrica (cuadro)
    """
    t2.setheading(0)
    t2.speed(0)
    if FIGURA_GLOBAL == "cuadro":
        for _ in range(4):
            t2.forward(lado)
            t2.left(90)
    elif FIGURA_GLOBAL == "círculo":
        t2.circle(lado / 2)

def mostrar_menu() -> None:
    """
    Función para mostrar el menú de opciones en la ventana gráfica
    """
    global FIGURA_GLOBAL
    FIGURA_GLOBAL = str(elegir_figura())
    t.hideturtle()
    t2.hideturtle()
    teleport_1t(-450, 350)
    fuente = ("Arial", 12, "bold")
    t.write("Práctica #2 - Graficación ITE Ensenada", font=fuente)
    teleport_1t(-450, 340)
    fuente_normal = ("Arial", 8, "normal")
    t.write("Presiona las siguientes teclas:", font=fuente_normal)
    opciones = [
        "◄ - Mover izquierda",
        "► - Mover derecha", 
        "▲ - Mover arriba",
        "▼ - Mover abajo",
        "ESC - Salir del programa"
    ]
    y_pos = 320
    for opcion in opciones:
        teleport_1t(-450, y_pos)
        t.write(opcion, font=fuente_normal)
        y_pos -= 20
    teleport_2t(COORDENADA_X,COORDENADA_Y)
    draw_something(50)

def walk_left() -> None:
    """
    Función para mover la figura a la izquierda
    """
    global COORDENADA_X
    t2.clear()
    COORDENADA_X -= 10
    teleport_2t(COORDENADA_X,COORDENADA_Y)
    draw_something(50)

def walk_right() -> None:
    """
    Función para mover la figura a la derecha
    """
    global COORDENADA_X
    t2.clear()
    COORDENADA_X += 10
    teleport_2t(COORDENADA_X,COORDENADA_Y)
    draw_something(50)

def walk_up() -> None:
    """
    Función para mover la figura hacia arriba
    """
    global COORDENADA_Y
    t2.clear()
    COORDENADA_Y += 10
    teleport_2t(COORDENADA_X,COORDENADA_Y)
    draw_something(50)

def walk_down() -> None:
    """
    Función para mover la figura hacia abajo
    """
    global COORDENADA_Y
    t2.clear()
    COORDENADA_Y -= 10
    teleport_2t(COORDENADA_X,COORDENADA_Y)
    draw_something(50)

def elegir_figura() -> str:
    """
    Función para elegir la figura a dibujar
    """
    screen = turtle.Screen()
    figura = screen.textinput("Elige","Elige la figura a dibujar (cuadro/círculo)")
    if figura == "cuadro":
        return "cuadro"
    if figura in ("círculo", "circulo"):
        return "círculo"
    print("Figura no reconocida. Se dibujará un cuadro por defecto.")
    return "circulo"
    