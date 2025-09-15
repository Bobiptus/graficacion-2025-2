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
import os
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
    os.system('cls')
    lado_triangulo = int(input("¿De que tamaño quieres el triangulo? "))
    lado_cuadro = int(input("¿De que tamaño quieres el cuadro? "))
    radio_circulo = int(input("¿De que tamaño quieres el circulo? "))
    raya = int(input("¿De que largo quieres el linea? "))
    angulo = int(input("¿En que angulo quieres el linea? "))
    navi.triangulo(lado_triangulo)
    navi.teleport(250,250)
    navi.cuadro(lado_cuadro)
    navi.teleport(-250,250)
    navi.circulo(radio_circulo)
    navi.teleport(-250,-250)
    navi.linea(raya, angulo)


main()
SCREEN.onkey(cerrar, "Escape")
SCREEN.listen()
SCREEN.mainloop()
