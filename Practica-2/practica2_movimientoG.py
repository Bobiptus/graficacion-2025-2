"""Practica 2: Movimiento de Navegacion
Usando turtle, crea una figura geométrica (cuadrado o círculo).
Programa las teclas para mover la figura:

    Flecha izquierda: mover en eje X hacia la izquierda.
    Flecha derecha: mover en eje X hacia la derecha.
    Flecha arriba: mover en eje Y hacia arriba.
    Flecha abajo: mover en eje Y hacia abajo.

Asegúrate de que la figura se mueva sin dejar rastro.
"""
import turtle as t
import Navi
SCREEN = t.Screen()
def cerrar ():
    """
    Funcion para cerrar ventana
    """
    SCREEN.bye()

def main ():
    """
    Funcion principal
    """
    Navi.mostrar_menu()
    SCREEN.onkey(Navi.walk_up,"Up")
    SCREEN.onkey(Navi.walk_down,"Down")
    SCREEN.onkey(Navi.walk_left,"Left")
    SCREEN.onkey(Navi.walk_right,"Right")
    SCREEN.onkey(cerrar, "Escape")

main()
SCREEN.listen()
SCREEN.mainloop()
