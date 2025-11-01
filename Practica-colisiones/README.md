# 🎮 Juego de Colisiones - Pygame

Un simple juego de disparos desarrollado en Python usando Pygame, donde el objetivo es destruir enemigos y acumular puntos.

## 📋 Descripción

Este es un juego básico de colisiones donde controlas un jugador verde que dispara balas amarillas para eliminar enemigos rojos. Cada vez que destruyes un enemigo, este reaparece en una nueva posición aleatoria y tu puntaje aumenta.

## 🚀 Características

- Sistema de disparos con barra espaciadora
- Detección de colisiones entre balas y enemigos
- Sistema de puntaje visible en pantalla
- Reaparición aleatoria de enemigos al ser destruidos
- Interfaz gráfica simple y funcional

## 🛠️ Requisitos

- Python 3.x
- Pygame

## 📦 Instalación

1. Asegúrate de tener Python instalado en tu sistema
2. Instala Pygame usando pip:

```bash
pip install pygame
```

3. Descarga el archivo del juego
4. Ejecuta el programa:

```bash
python nombre_del_archivo.py
```

## 🎯 Cómo jugar

- **Barra espaciadora**: Disparar balas
- **Objetivo**: Destruir enemigos para aumentar tu puntaje
- **Cerrar ventana**: Terminar el juego

## 🔧 Modificaciones realizadas

Este código fue modificado a partir de una versión base. Los cambios implementados son:

1. **Sistema de fuente (línea 7)**: Se agregó `font = pygame.font.Font(None, 36)` para establecer la fuente del texto del puntaje

2. **Incremento de puntaje (línea 25)**: Se implementó `SCORE += 1` para aumentar el puntaje cada vez que una bala colisiona con un enemigo

3. **Posición aleatoria de enemigos (línea 28)**: Se agregó `x = random.randint(100, 360)` para generar una nueva posición x aleatoria cuando un enemigo es destruido

4. **Reaparición de enemigos (línea 29)**: Se implementó `enemigos.append(pygame.Rect(x, 300, 40, 40))` para que el enemigo reaparezca inmediatamente después de ser destruido en una nueva posición

5. **Visualización del puntaje (líneas 34-35)**: Se agregaron las líneas para renderizar y mostrar el puntaje en la esquina superior izquierda de la pantalla:
   ```python
   text_surface = font.render(f"SCORE: {SCORE}", True, (255, 255, 255))
   pantalla.blit(text_surface, (10, 10))
   ```

## 📊 Especificaciones técnicas

- **Resolución**: 600x400 píxeles
- **FPS**: 30 frames por segundo
- **Tamaño del jugador**: 40x40 píxeles (verde)
- **Tamaño de las balas**: 10x5 píxeles (amarillo)
- **Tamaño de los enemigos**: 40x40 píxeles (rojo)
- **Velocidad de las balas**: 10 píxeles por frame

## 🎨 Colores utilizados

- **Fondo**: Negro (0, 0, 0)
- **Jugador**: Verde (0, 255, 0)
- **Balas**: Amarillo (255, 255, 0)
- **Enemigos**: Rojo (255, 0, 0)
- **Texto del puntaje**: Blanco (255, 255, 255)

## 📝 Notas

- Los enemigos siempre aparecen en la posición vertical y=300
- El rango de aparición horizontal de los enemigos es entre x=100 y x=360
- Las balas desaparecen automáticamente al salir de la pantalla
- El juego no tiene límite de tiempo ni condición de victoria/derrota

## 👨‍💻 Autor

[Tu nombre aquí]

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

**Versión**: 1.0  
**Última actualización**: Octubre 2025
