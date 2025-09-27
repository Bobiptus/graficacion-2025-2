"""
Esta biblioteca contiene todas las funciones de dibujo geométrico disponibles para
el sistema. Utiliza la biblioteca turtle de Python para crear gráficos vectoriales
en una ventana de dibujo. Cada función está optimizada para crear figuras geométricas
básicas con precisión y consistencia visual.

FUNCIONES DISPONIBLES:
=====================

1. cuadro(lado_cara: float)
   - Dibuja un cuadrado perfecto con lados iguales
   - Orientación: Inicia desde la posición actual hacia la derecha (0°)
   - Dirección de dibujo: Sentido antihorario
   - Parámetro: lado_cara = longitud de cada lado en píxeles

2. triangulo(lado_cara: float)  
   - Dibuja un triángulo equilátero (todos los lados iguales)
   - Orientación: Inicia desde la posición actual hacia la derecha (0°)
   - Ángulos internos: 60° cada uno
   - Parámetro: lado_cara = longitud de cada lado en píxeles

3. circulo(radio: float)
   - Dibuja un círculo usando aproximación poligonal (60 segmentos)
   - Orientación: Inicia desde la posición actual hacia la derecha (0°)
   - Método: Divide la circunferencia en 60 pasos para suavidad visual
   - Parámetro: radio = radio del círculo en píxeles
   - Fórmula: Circunferencia = 2πr, dividida en 60 segmentos iguales

4. teleport(x: float, y: float)
   - Mueve la tortuga a coordenadas específicas sin dibujar líneas
   - Levanta el lápiz, se mueve, y baja el lápiz automáticamente
   - Sistema de coordenadas: Centro de pantalla = (0,0)
   - Parámetros: x = posición horizontal, y = posición vertical

CARACTERÍSTICAS TÉCNICAS:
========================

SISTEMA DE COORDENADAS:
- Origen (0,0): Centro de la pantalla de dibujo
- Eje X: Positivo hacia la derecha, negativo hacia la izquierda  
- Eje Y: Positivo hacia arriba, negativo hacia abajo
- Rango recomendado: -300 a +300 píxeles en cada eje

ORIENTACIÓN DE LA TORTUGA:
- Todas las figuras inician con orientación 0° (hacia la derecha)
- Se restablece la orientación antes de cada dibujo para consistencia
- Los ángulos se miden en sentido antihorario desde la horizontal derecha

PRECISIÓN DEL CÍRCULO:
- Utiliza 60 segmentos para aproximar la curvatura
- Cada segmento representa 6° del círculo total (360°/60)
- La longitud de cada segmento se calcula como: (2πr)/60
- Valor de π aproximado: 3.14159

ESTADO DEL LÁPIZ:
- Todas las funciones de dibujo asumen que el lápiz está bajado (pendown)
- Solo teleport manipula el estado del lápiz (up/down)
- Las funciones mantienen el lápiz en posición de dibujo al finalizar
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
