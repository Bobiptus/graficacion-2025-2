import turtle
import Tools

COORDENADA_X = 0
COORDENADA_Y = 0

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

#Se configura la pantalla
screen = turtle.Screen()
screen.title("Mi dibujo con Turtle")
screen.bgcolor("white")    
screen.setup(width=600, height=600)  

def main():
    """
    Funcion principal que lee el archivo y lo convierte en una cadena para su análisis
    """
    contador_pixeles = 0 
    global COORDENADA_X, COORDENADA_Y
    filename = "imagen.txt"
    for line in open(filename):
        seq = line.split()
        if seq:  #Esta condición revisa si aún hay caracteres en el archivo
            for w in seq[0]: #Esta condición es para saber si no hemos terminado la cadena
                if w and int(w) != 0: #Esta condición es para no imprimir en color blanco
                    color_pixel = Tools.revisa_color(int(w))
                    Tools.print_dot(COORDENADA_X, COORDENADA_Y, color_pixel)
                
                COORDENADA_X = COORDENADA_X + 1
                contador_pixeles = contador_pixeles + 1
                
                if (contador_pixeles == 100): #Condición para brincar de renglón
                    contador_pixeles = 0
                    COORDENADA_X = 0
                    COORDENADA_Y = COORDENADA_Y - 1
        else:
            return


COORDENADA_X = -100  
COORDENADA_Y = 100   

main()

screen.exitonclick()