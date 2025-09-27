"""
Este módulo actúa como el controlador principal para ejecutar los comandos de dibujo
detectados en el archivo de texto. Valida los parámetros de entrada y ejecuta las
funciones correspondientes del módulo 'instrucciones'.

FUNCIONALIDAD PRINCIPAL:
- Valida que los comandos tengan los parámetros correctos
- Verifica que las dimensiones estén dentro de los rangos permitidos
- Ejecuta las instrucciones de dibujo correspondientes
- Maneja errores de conversión de tipos y valores fuera de rango

VALIDACIONES IMPLEMENTADAS:
1. Tamaño de figuras: debe ser > 0 y ≤ 300 píxeles
2. Coordenadas de teleport: deben estar entre -300 y 300
3. Comando teleport: requiere obligatoriamente dos coordenadas
4. Conversión de tipos: maneja errores de valores no numéricos

COMANDOS SOPORTADOS:
- circulo <radio>: Dibuja un círculo con el radio especificado
- cuadro <lado>: Dibuja un cuadrado con el lado especificado  
- triangulo <lado>: Dibuja un triángulo equilátero con el lado especificado
- teleport <x>,<y>: Mueve la tortuga a las coordenadas especificadas sin dibujar
"""
import instrucciones

def opciones(cadena_temporal: str, tamano_figura: str, segunda_coordenada: str) -> None:
    """
    
    """
    try:
        figura = int(tamano_figura)
        coordenada = int(segunda_coordenada) if segunda_coordenada else 0

        if figura > 300:
            print("Dimensiones fuera de rango")
            return

        if figura <= 0:
            print("El tamaño debe ser mayor que 0")
            return

        if cadena_temporal == "teleport" and (coordenada > 300 or coordenada < -300):
            print("Coordenadas fuera de rango")
            return
        if cadena_temporal == 'circulo':
            instrucciones.circulo(figura)
        elif cadena_temporal == "cuadro":
            instrucciones.cuadro(figura)
        elif cadena_temporal == "triangulo":
            instrucciones.triangulo(figura)
        elif cadena_temporal == "teleport":
            if segunda_coordenada:
                instrucciones.teleport(figura, coordenada)
            else:
                print("Teleport requiere dos coordenadas")
        else:
            print("Instruccion no reconocida")
 
    except ValueError:
        print("Error: Los valores deben ser números válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")
