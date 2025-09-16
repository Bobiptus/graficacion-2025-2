"""
Libreria creada para realizar la practica #1, se hace libreria
nueva para tener un codigo mas limpio en el archivo principal
"""
import turtle
t = turtle.Turtle()

def jump() -> None:
    """
    Funcion para mover el puntero sin dibujar y preguntando los valores
    """
    respuesta_x = turtle.textinput("Coordenda X","Ingresa las nuevas coordenadas X (Vacio = 0): ")
    if respuesta_x is None or respuesta_x == '':
        x = 0
    else:
        try:
            x = int(respuesta_x)
        except ValueError:
            x = 0
    respuesta_y = turtle.textinput("Coordenda Y","Ingresa las nuevas coordenadas Y (Vacio = 0): ")
    if respuesta_y is None or respuesta_y == '':
        y = 0
    else:
        try:
            y = int(respuesta_y)
        except ValueError:
            y = 0
    teleport(x,y)

def colorea() -> None:
    """
    Funcion para asignar color al puntero
    """
    color = turtle.textinput("Color","Colores disponibles [red, blue, green, purple] ")
    if color is None:
        color = "black"
    if color not in ["red", "blue", "green", "purple"]:
        color = "black"
    t.color(color)

def teleport(x:float, y:float) -> None:
    """
    Funcion para mover el puntero sin dibujar
    """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def cuadro(lado_cara:float) -> None:
    """
    Funcion para dibujar un cuadro
    """
    t.setheading(0)
    for _ in range(4):
        t.forward(lado_cara)
        t.left(90)

def triangulo(lado_cara:float) -> None:
    """
    Funcion para dibujar un triangulo
    """
    t.setheading(0)
    for _ in range (2):
        t.forward(lado_cara)
        t.left(120)
    t.forward(lado_cara)

def circulo(radio:float) -> None:
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

def linea(largo:int, angulo:float) -> None:
    """
    Funcion para dibujar una linea
    """
    t.speed(10)
    t.left(angulo)
    t.forward(largo)
    

def mostrar_menu() -> str:
    """
    Función para mostrar el menú de opciones en la ventana gráfica
    """
    t.color("black")
    teleport(-450, 350)
    fuente = ("Arial", 12, "bold")
    t.write("Práctica #1 - Graficación ITE Ensenada", font=fuente)
    teleport(-450, 340)
    fuente_normal = ("Arial", 8, "normal")
    t.write("Presiona las siguientes teclas:", font=fuente_normal)
    opciones = [
        "1 - Dibujar cuadrado",
        "2 - Dibujar triángulo", 
        "3 - Dibujar círculo",
        "4 - Dibujar línea",
        "0 - Limpiar pantalla",
        "5 - Salir del programa"
    ]
    y_pos = 320
    for opcion in opciones:
        teleport(-450, y_pos)
        t.write(opcion, font=fuente_normal)
        y_pos -= 20
    t.hideturtle()
    respuesta = turtle.textinput("Selecciona una opción", "Ingresa el número de la opción deseada:")
    if respuesta is None:
        return '5'
    try:
        return int(respuesta)
    except ValueError:
        return 0

def dibuja(figura:int) -> None:
    """
    Funcion para pedir los datos de la figura a dibujar
    """
    if figura == 1:
        respuesta = turtle.textinput("Tamaño","Ingresa el lado del cuadrado: ")
        if respuesta is None:
            return
        try:
            lado_cara = float(respuesta)
        except ValueError:
            return
        jump()
        colorea()
        cuadro(lado_cara)
    elif figura == 2:
        respuesta = turtle.textinput("Tamaño","Ingresa el lado del triangulo: ")
        if respuesta is None:
            return
        try:
            lado_cara = float(respuesta)
        except ValueError:
            return
        jump()
        colorea()
        triangulo(lado_cara)
    elif figura == 3:
        respuesta = turtle.textinput("Tamaño","Ingresa el radio del circulo: ")
        if respuesta is None:
            return
        try:
            radio = float(respuesta)
        except ValueError:
            return

        jump()
        colorea()
        circulo(radio)
    elif figura == 4:
        respuesta = turtle.textinput("Tamaño","Ingresa el largo de la linea: ")
        if respuesta is None:
            return
        try:
            largo = float(respuesta)
        except ValueError:
            return
        respuesta = turtle.textinput("Angulo","Ingresa el angulo de la linea: ")
        if respuesta is None:
            return
        try:
            angulo = float(respuesta)
        except ValueError:
            return
        jump()
        colorea()
        linea(largo, angulo)
    elif figura == 5:
        teleport(-50,-350)
        t.write("Presiona <ESC>", font=("Arial", 16, "bold"))
    elif figura == 0:
        t.clear()
    else:
        print("Opcion no valida")

