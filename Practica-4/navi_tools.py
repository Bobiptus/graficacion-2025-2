import opciones_menu

def detectar(contador: int, contenido: str):
    indice = 0
    cadena_temporal = ''
    numero_temporal = ''
    segunda_coordenada = ''
   
    while indice < contador:
        if contenido[indice] == ' ':
            indice += 1
            continue
        elif contenido[indice] == '\n':
            if numero_temporal:
                opciones_menu.opciones(cadena_temporal, numero_temporal, segunda_coordenada)
            elif cadena_temporal != '':
                print("Instruccion no reconocida")
           
            numero_temporal = ''
            cadena_temporal = ''
            segunda_coordenada = ''
        else:
            if ('A' <= contenido[indice] <= "Z") or ('a' <= contenido[indice] <= "z"):
                cadena_temporal += contenido[indice]
            elif ('0' <= contenido[indice] <= '9'):
                numero_temporal += contenido[indice]
            elif contenido[indice] == '-':
                if numero_temporal == '':
                    numero_temporal += contenido[indice]
                else:
                    print("Caracter no reconocido")
            elif contenido[indice] == '.':
                numero_temporal += contenido[indice]
            elif contenido[indice] == ',':
                indice += 1

                while indice < contador and contenido[indice] == ' ':
                    indice += 1

                if indice < contador and contenido[indice] == '-':
                    segunda_coordenada += contenido[indice]
                    indice += 1

                while indice < contador and (('0' <= contenido[indice] <= '9') or contenido[indice] == '.'):
                    segunda_coordenada += contenido[indice]
                    indice += 1
                
                indice -= 1
            else:
                print("Caracter no reconocido")
       
        if indice == contador - 1:
            if numero_temporal:
                opciones_menu.opciones(cadena_temporal, numero_temporal, segunda_coordenada)
            elif cadena_temporal != '':
                print("Instruccion no reconocida")
       
        indice += 1
