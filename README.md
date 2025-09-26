# Proyecto de Graficación con Turtle - Práctica 1

## Descripción

Este proyecto es una práctica de la clase de Graficación en el ITE Ensenada. Utiliza el módulo `turtle` para dibujar varias figuras geométricas básicas: un cuadrado, un triángulo, un círculo y una línea recta. Cada figura está implementada como una función que recibe parámetros como coordenadas iniciales, tamaño y color para personalizar el dibujo.

## Funcionalidades

- Dibuja un cuadrado con lado y color especificados.
- Dibuja un triángulo con lado y color especificados.
- Dibuja un círculo con radio y color especificados.
- Dibuja una línea recta con largo, ángulo y color especificados.
- Interfaz de menú para seleccionar la figura a dibujar o limpiar la pantalla.
- La ventana se cierra con la tecla Escape.

## Uso

1. Ejecuta el archivo principal `practica1_figurasG.py`.
2. Selecciona con qué figura deseas interactuar mediante la ventana de opciones.
3. Ingresa los parámetros solicitados para la figura (tamaño, coordenadas, color, etc.).
4. Disfruta del dibujo generado en la ventana de turtle.
5. Presiona Escape para salir y cerrar la ventana.

## Requisitos

- Python 3.x (probado exitosamente en 3.10 y 3.12)
- Módulo `turtle` (incluido en la biblioteca estándar de Python)

## Archivos

- `navi.py`: Biblioteca con funciones para controlar el turtle, dibujar figuras y manejar la interfaz.
- `practica1_figurasG.py`: Archivo principal que utiliza la biblioteca y lanza la aplicación gráfica.

## Autor

Armando Roberto Pérez Banda
Control: 24760228

# Práctica 2: Movimiento de Navegación

## Descripción

Este proyecto utiliza la librería `turtle` de Python para crear una figura geométrica interactiva que puede ser controlada mediante las teclas de dirección del teclado.

## Características

- Creación de figuras geométricas (cuadrado o círculo)
- Control de movimiento mediante teclas de dirección
- Interfaz gráfica con menú de instrucciones
- Movimiento sin dejar rastro de la figura

## Archivos del Proyecto

- `practica2_movimientoG.py` - Archivo principal del programa
- `Navi.py` - Módulo con las funciones de navegación y dibujo

## Requisitos

- Python 3.x (probado exitosamente en 3.10 y 3.12)
- Librería turtle (incluida por defecto en Python)

## Instrucciones de Uso

### Ejecución

```bash
python practica2_movimientoG.py
```

### Controles

- **Flecha Izquierda (◄)**: Mover la figura hacia la izquierda en el eje X
- **Flecha Derecha (►)**: Mover la figura hacia la derecha en el eje X
- **Flecha Arriba (▲)**: Mover la figura hacia arriba en el eje Y
- **Flecha Abajo (▼)**: Mover la figura hacia abajo en el eje Y
- **ESC**: Cerrar el programa

### Selección de Figura

Al iniciar el programa, se mostrará un cuadro de diálogo donde podrás elegir entre:

- `cuadro` - Para dibujar un cuadrado
- `círculo` o `circulo` - Para dibujar un círculo

## Funcionalidades Técnicas

### Módulo Principal (`practica2_movimientoG.py`)

- Inicialización de la ventana gráfica
- Configuración de eventos de teclado
- Función de cierre del programa

### Módulo de Navegación (`Navi.py`)

- `mostrar_menu()`: Muestra las instrucciones en pantalla
- `elegir_figura()`: Permite seleccionar la figura a dibujar
- `walk_left()`, `walk_right()`, `walk_up()`, `walk_down()`: Funciones de movimiento
- `draw_something()`: Dibuja la figura seleccionada
- `teleport_1t()`, `teleport_2t()`: Funciones auxiliares para posicionamiento

## Características del Movimiento

- La figura se mueve en incrementos de 10 unidades
- El movimiento se realiza sin dejar rastro (la figura anterior se borra)
- Las coordenadas se actualizan globalmente para mantener la posición

# Práctica 3: Lectura de Archivo Numérico y Pintado con Turtle

## Descripción

En esta práctica se implementa un programa que lee un archivo de texto (`imagen.txt`) que contiene únicamente números del 0 al 9. Cada número corresponde a un color de una paleta definida, y el programa utiliza la librería `turtle` para pintar una matriz de **100x100 píxeles** en la ventana gráfica.

El objetivo es graficar la imagen codificada en el archivo numérico, asignando a cada dígito un color específico.

## Paleta de Colores

- 0 → Blanco
- 1 → Negro
- 2 → Verde
- 3 → Rojo
- 4 → Amarillo
- 5 → Púrpura
- 6 → Azul
- 7 → Cyan
- 8 → Chartreuse
- 9 → Deep Pink

## Archivos del Proyecto

- `practica3_archivo_numericoG.py`: Programa principal que lee el archivo numérico y pinta la imagen.
- `Tools.py`: Biblioteca auxiliar con funciones para posicionar el puntero, pintar píxeles y traducir números a colores.
- `imagen.txt`: Archivo de entrada que contiene la matriz de números.

## Requisitos

- Python 3.x (probado exitosamente en 3.10 y 3.12)
- Librería `turtle` (incluida por defecto en Python)

## Instrucciones de Uso

1. Coloca un archivo `imagen.txt` en el mismo directorio del programa.
   - El archivo debe contener **100 líneas con 100 números cada una** (valores entre 0 y 9).
2. Ejecuta el programa con:

   ```bash
   python practica3_archivo_numericoG.py
   ```

## Autor

Armando Roberto Pérez Banda
Control: 24760228
