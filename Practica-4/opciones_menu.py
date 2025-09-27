import instrucciones

def opciones(cadena_temporal: str, tamano_figura: str, segunda_coordenada: str) -> None:
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