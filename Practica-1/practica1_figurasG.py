"""
Practica #1 de la clase de Graficacion en el ITE Ensenada
Usando el módulo turtle, dibuja:

 - Un cuadrado.
 - Un triángulo.
 - Un círculo.
 - Una línea recta.
Cada figura debe ser una funcion, que reciba como parametros
coordenadas inicials y finales si es que la figura lo requiere,
ademas poder asignarle el color a dibujar.
"""
import turtle
import navi
SCREEN = turtle.Screen()

def cerrar ():
    """
    Funcion para cerrar ventana
    """
    SCREEN.bye()

def main ():
    """
    Funcion principal
    """
    opcion = int(navi.mostrar_menu())
    navi.dibuja(opcion)
    if opcion != 5:
        main()

main()
SCREEN.onkey(cerrar, "Escape")
SCREEN.listen()
SCREEN.mainloop()
