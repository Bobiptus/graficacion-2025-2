import turtle
import Tools

COORDENADA_X = 0
COORDENADA_Y = 0

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

screen = turtle.Screen()
screen.title("Mi dibujo con Turtle")
screen.bgcolor("white")    
screen.setup(width=100, height=100)  

def leer_archivo():
    contador_pixeles = 0 
    global COORDENADA_X, COORDENADA_Y
    filename = "imagen.txt"
    for line in open(filename):
        seq = line.split()
        if seq:
            for w in seq[0]:
                if w and int(w) != 0:
                    color_pixel = Tools.revisa_color(int(w))
                    Tools.print_dot(COORDENADA_X, COORDENADA_Y, color_pixel)
                
                COORDENADA_X = COORDENADA_X + 1
                contador_pixeles = contador_pixeles + 1
                
                if (contador_pixeles == 100):
                    contador_pixeles = 0
                    COORDENADA_X = 0
                    COORDENADA_Y = COORDENADA_Y - 1
        else:
            return


COORDENADA_X = -50  
COORDENADA_Y = 50   

leer_archivo()

screen.exitonclick()