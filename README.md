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

Práctica 4: Sistema de Dibujo Automatizado por Comandos de Texto
Descripción
Este proyecto implementa un sistema de dibujo automatizado que lee comandos desde un archivo de texto (dibujante.txt) y los convierte en gráficos vectoriales usando la biblioteca Turtle de Python. El sistema utiliza una arquitectura modular con analizador léxico, controlador de comandos y biblioteca de funciones de dibujo.
Arquitectura del Sistema
Módulos Componentes:

practica4_archivo_instruccionesG.py - Programa principal y configuración del entorno gráfico
navi_tools.py - Analizador léxico de comandos de texto
opciones_menu.py - Controlador de comandos y validador de parámetros
instrucciones.py - Biblioteca de funciones de dibujo geométrico

Flujo de Ejecución:

[INICIO] Configuración del entorno gráfico
[LECTURA] Carga completa del archivo de comandos
[PROCESAMIENTO] Análisis léxico línea por línea
[VALIDACIÓN] Verificación de sintaxis y rangos
[EJECUCIÓN] Dibujo de figuras geométricas
[FINALIZACIÓN] Espera por clic para cerrar

Comandos Soportados

circulo <radio>: Dibuja un círculo con el radio especificado
cuadro <lado>: Dibuja un cuadrado con el lado especificado
triangulo <lado>: Dibuja un triángulo equilátero con el lado especificado
teleport <x>,<y>: Mueve la tortuga a las coordenadas especificadas sin dibujar

Reglas del Formato de Archivo de Entrada
Estructura General:

Una instrucción por línea
Formato: <comando> <parámetro1>[,<parámetro2>]
Las líneas vacías se ignoran
Los espacios en blanco al inicio y final de línea se ignoran

Ejemplos de Formato Válido:
circulo 50
cuadro 100
triangulo 75
teleport 150,-100
circulo 25.5
teleport -200,200

Validaciones Implementadas:

Tamaño de figuras: debe ser > 0 y ≤ 300 píxeles
Coordenadas de teleport: deben estar entre -300 y 300
Comando teleport: requiere obligatoriamente dos coordenadas
Conversión de tipos: maneja errores de valores no numéricos

Características Técnicas
Sistema de Coordenadas:

Origen (0,0): Centro de la pantalla de dibujo
Eje X: Positivo hacia la derecha, negativo hacia la izquierda
Eje Y: Positivo hacia arriba, negativo hacia abajo
Rango recomendado: -300 a +300 píxeles en cada eje

Precisión del Círculo:

Utiliza 60 segmentos para aproximar la curvatura
Cada segmento representa 6° del círculo total (360°/60)
La longitud de cada segmento se calcula como: (2πr)/60

Orientación de la Tortuga:

Todas las figuras inician con orientación 0° (hacia la derecha)
Se restablece la orientación antes de cada dibujo para consistencia
Los ángulos se miden en sentido antihorario desde la horizontal derecha

Uso

Crea un archivo dibujante.txt en el mismo directorio del programa
Escribe los comandos de dibujo siguiendo el formato especificado

Ejecuta el programa principal:
python practica4_archivo_instruccionesG.py

Requisitos del Sistema

Python 3.x (probado exitosamente en 3.10 y 3.12)
Módulo turtle (incluido en la biblioteca estándar de Python)

Instalación y Ejecución

Clona o descarga este repositorio
Navega al directorio del proyecto que desees ejecutar
Asegúrate de tener los archivos de entrada necesarios (según la práctica)
Ejecuta el archivo principal de Python correspondiente

Estructura del Repositorio
├── practica1_figurasG.py
├── navi.py
├── practica2_movimientoG.py
├── Navi.py
├── practica3_archivo_numericoG.py
├── Tools.py
├── imagen.txt
├── practica4_archivo_instruccionesG.py
├── navi_tools.py
├── opciones_menu.py
├── instrucciones.py
├── dibujante.txt
└── README.md
