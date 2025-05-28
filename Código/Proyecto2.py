import random
import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk, ImageOps  


##########################################interfaz###############################################################################
def ventanaInicio():

    global root

    root = tk.Tk() 
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.resizable(False, False)
    root.title("Tectris")

    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()

    imagenFondoInicio = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\fondoIncio.png")
    imagenFondoInicio = imagenFondoInicio.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondoInicio = ImageTk.PhotoImage(imagenFondoInicio)

    labelFondoInicio = tk.Label(root, image=fondoInicio)
    labelFondoInicio.place(x=0, y=0, relwidth=1, relheight=1)

    iniciar = tk.Label(root, text="Press Enter for Start", font="pixellance", background="black", fg="White")
    iniciar.place(x=500, y=500, width=500, height=100)

    root.bind("<Return>", lambda e: ventanaPrincipal(e))


    root.mainloop()

def ventanaPrincipal(e):

    imagenFondo = Image.open(r"C:/Users/geyer/OneDrive/Escritorio/TEC/Progra/semestre3/taller/Proyecto#2/fondo.jpg")
    fondoPrincipal = ImageTk.PhotoImage(imagenFondo)

    labelFondoPrincipal = tk.Label(root, image=fondoPrincipal)
    labelFondoPrincipal.place(x=0, y=0, relwidth=1, relheight=1)

    boton_modo_normal = Button(root, text="Modo Normal", width=25, height=5, command=matriz)
    boton_modo_normal.place(x=670, y=250)


piezaActual = None
posicionActual = (0, 5)  # Posición inicial (fila, columna)
rotaciones = {pieza: 0 for pieza in ['I', 'J', 'L', 'O', 'S', 'T', 'Z']}
puntajeTotal = 0


formas = {
    1: [(0,0), (0,1), (1,0), (1,1)],
    2: [(0,0), (1,0), (2,0)],
    3: [(0,0), (1,0), (2,0), (2,1)],
    4: [(0,1), (1,1), (2,1), (2,0)],
    5: [(0,0), (0,1), (0,2), (1,1)],
    6: [(0,0), (0,1), (1,1), (1,2)],
    7: [(0,0), (1,0), (1,1), (1,2), (0,2)],
    8: [(0,1), (1,0), (1,1), (1,2), (2,1)],
    }

global imagenes 
imagenes = {}

imagenes["borde"] = imagenBorde = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\borde.png").resize((30, 30))
imagenes["Q"] = imagenQ = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueNaranja.png").resize((30, 30))
imagenes["I"] = imagenI = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueAmarillo.png").resize((30, 30))
imagenes["L"] = imagenL = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueAzul.png").resize((30, 30))
imagenes["J"] = imagenJ = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueMorado.png").resize((30, 30))
imagenes["T"] = imagenT = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueRojo.png").resize((30, 30))
imagenes["Z"] = imagenZ = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueVerdeClaro.png").resize((30, 30))
imagenes["U"] = imagenU = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueVerde.png").resize((30, 30))


"""
Nombre: matriz
Entrada: 
Salida: Retorna una matriz de 22x12 y guarda cada una de las casillas con su respectivo valor en un diccionario
Restricciones: 
"""
def matriz():
    global valores
    valores = {}

    frameTablero = tk.LabelFrame(root, text="Tectris", padx=10, pady=10)
    frameTablero.pack(padx=20, pady=20)

    global celdas
    celdas = {}

    for fila in range(22):
        for columna in range(12):
            label = tk.Label(frameTablero, width=3, height=1, bd=1, relief="solid", bg="black")
            label.grid(row=fila, column=columna)
            celdas[(fila, columna)] = label

            if (columna == 0) or (columna == 11) or (fila == 0) or (fila == 21):
                valores[(fila, columna)] = "+"
                borde = ImageTk.PhotoImage(imagenBorde)
                label.config(image=borde)
                label.image = borde 
            else:
                valores[(fila, columna)] = 0
"""
Nombre: generarPieza
Entrada:
Salida: Retorna un tetronimo aleatorio
Restricciones:
"""
def generarPieza():
    piezas = ["I", "J", "L", "O", "S", "T", "Z", "U"]
    return random.choice(piezas)


"""
Nombre: ponerPiezas
Entrada: la pieza y las coordenadas en la matriz
Salida: 
Restricciones:
"""
def ponerPiezas(pieza, fila, columna):
    global valores
    forma = formas[pieza]
    
    for x1, y1 in forma:
        x2, y2 = fila + x1, columna + y1
        if 0 <= x2 < 22 and 0 <= y2 < 12:
            valores[(x2, y2)] = 1
            img = ImageTk.PhotoImage(imagenes[pieza])
            botones[(x2, y2)].config(image=img)
            botones[(x2, y2)].image = img  


"""
Nombre: moverPieza
Entrada: La direccion a la cual se desea mover la pieza
Salida: Confirmar que el movimiento se puede hacer
Restricciones: El parámetro debe ser un movimiento valido
"""
def moverPieza(direccion):
    global piezaActual, posicionActual
    
    nuevaPosicion = nuevaPosicionPieza(posicionActual, direccion)
    
    if verificarColision(nuevaPosicion):
        return False
    
    posicionActual = nuevaPosicion
    actualizarTablero()
    return True

"""
Nombre: nuevaPosicionPieza
Entrada: La posicion actual y la direccion que se quiere mover
Salida: mueve la pieza de posicion en la matriz
Restricciones: los parámetros deben ser validos
"""
def nuevaPosicionPieza(posicion, direccion):
    x, y = posicion
    if direccion == 'izquierda':
        return (x, y-1)
    elif direccion == 'derecha':
        return (x, y+1)
    elif direccion == 'abajo':
        return (x+1, y)
    return posicion

"""
Nombre: verificarColision
Entrada: la posicion a la cual se quiere haccer el movimiento
Salida: True si 
"""
def verificarColision(nuevaPosicion):
    x, y = nuevaPosicion
    formaActual = formas[piezaActual][rotaciones[piezaActual]]
    
    for x1, y1 in formaActual:
        x2, y2 = x + x1, y + y1
        if x2 < 0 or x2 >= 22 or y2 < 0 or y2 >= 12 or valores[(x2, y2)] != 0:
            return True
    return False


"""
Nombre: puntaje
Entrada: Recibira fila 
Salida: Cada vez que el jugador limpie una fila retornará 100 puntos
Restricciones:
"""
def puntaje(fila):

    return 100     



    


    
ventanaInicio()