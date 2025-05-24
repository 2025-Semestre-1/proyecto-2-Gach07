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

    global botones
    botones = {}

    for fila in range(22):
        for columna in range(12):

            button = tk.Button(frameTablero, width=3, height=1)
            button.grid(row=fila, column=columna)
            botones[(fila, columna)] = button

            if (columna == 0) or (columna == 11) or (fila == 0) or (fila == 21):
                valores[(fila, columna)] = "+"
                borde = ImageTk.PhotoImage(imagenBorde)
                button.config(image=borde)
            else:
                valores[(fila, columna)] = 0

"""
Nombre: ponerPiezas
Entrada:
Salida:
Restricciones:
"""
#def ponerPiezas(tablero, pieza, fila, columna):

    #for coorX, coorY in matriz:



    






"""
Nombre: puntaje
Entrada: Recibira fila 
Salida: Cada vez que el jugador limpie una fila retornará 100 puntos
Restricciones:
"""
def puntaje(fila):

    return 100     



    


    
ventanaInicio()
