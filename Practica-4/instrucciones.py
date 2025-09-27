"""
Este es el programa principal de un sistema de dibujo automatizado que lee comandos
desde un archivo de texto y los convierte en gráficos vectoriales usando la biblioteca
Turtle de Python. El sistema está diseñado para ser educativo, permitiendo crear
dibujos complejos mediante instrucciones de texto simples.

ARQUITECTURA DEL SISTEMA:
========================

MÓDULOS COMPONENTES:
1. practica4_archivo_instruccionesG.py (ESTE ARCHIVO) - Programa principal
2. navi_tools.py - Analizador léxico de comandos de texto  
3. opciones_menu.py - Controlador de comandos y validador
4. instrucciones.py - Biblioteca de funciones de dibujo

FLUJO DE EJECUCIÓN:
==================
1. [INICIO] Configuración del entorno gráfico
2. [LECTURA] Carga completa del archivo de comandos
3. [PROCESAMIENTO] Análisis léxico línea por línea
4. [VALIDACIÓN] Verificación de sintaxis y rangos
5. [EJECUCIÓN] Dibujo de figuras geométricas
6. [FINALIZACIÓN] Espera por clic para cerrar
"""
import turtle
t = turtle.Turtle()

def cuadro(lado_cara:float) -> None:
    """
    Función para dibujar un cuadro
    """
    t.setheading(0)
    for _ in range(4):
        t.forward(lado_cara)
        t.left(90)

def triangulo(lado_cara:float) -> None:
    """
    Función para dibujar un triángulo
    """
    t.setheading(0)
    for _ in range (2):
        t.forward(lado_cara)
        t.left(120)
    t.forward(lado_cara)

def circulo(radio:float) -> None:
    """
    Función para dibujar un círculo
    """
    t.setheading(0)
    pasos = 60
    avance = (2 * 3.14159 * radio) / pasos
    angulo = 360 / pasos
    for _ in range(pasos):
        t.forward(avance)
        t.left(angulo)

def teleport(x:float, y:float) -> None:
    """
    Función para mover el puntero sin dibujar
    """
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()
