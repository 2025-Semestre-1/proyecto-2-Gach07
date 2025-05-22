import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk, ImageOps  

"""
Nombre: matriz
Entrada: 
Salida: Retorna una matriz de 22x12 y guarda cada una de las casillas con su respectivo valor en un diccionario
Restricciones: 
"""


def matriz():
    valores = {}
    frameTablero = tk.LabelFrame(root, text="Tetris", padx=10, pady=10)
    frameTablero.pack(padx=20, pady=20)

    for fila in range(22):
        for columna in range(12):
            button = tk.Button(frameTablero, width=3, height=1)
            button.grid(row=fila, column=columna)

            if (columna == 1) or (columna == 12) or (fila == 1) or (fila == 22):
                valores[button] = "+"
            else:
                valores[button] = 0
    
            

"""
Nombre: puntaje
Entrada: Recibira fila 
Salida: Cada vez que el jugador limpie una fila retornará 100 puntos
Restricciones:
"""
def puntaje(fila):

    return 100     



##########################################interfaz###############################################################################
def ventanaInicio():

    global root

    root = tk.Tk() 
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.resizable(False, False)
    root.title("Tetris: La venganza del TEC")

    ancho = root.winfo_screenwidth()
    alto = root.winfo_screenheight()

    imagenFondoInicio = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\fondoIncio.png")
    imagenFondoInicio = imagenFondoInicio.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondoInicio = ImageTk.PhotoImage(imagenFondoInicio)

    labelFondoInicio = tk.Label(root, image=fondoInicio)
    labelFondoInicio.place(x=0, y=0, relwidth=1, relheight=1)

    iniciar = tk.Label(root, text="Press Enter for Start", font="pixellance", background="black", fg="White")
    iniciar.place(x=500, y=500, width=500, height=100)

    root.bind("<Return>", lambda e: ventanaPrincipal())


    root.mainloop()

def ventanaPrincipal(e):

    imagenFondo = Image.open(r"C:/Users/geyer/OneDrive/Escritorio/TEC/Progra/semestre3/taller/Proyecto#2/fondo.jpg")
    fondoPrincipal = ImageTk.PhotoImage(imagenFondo)

    labelFondoPrincipal = tk.Label(root, image=fondoPrincipal)
    labelFondoPrincipal.place(x=0, y=0, relwidth=1, relheight=1)

    boton_modo_normal = Button(root, text="Modo Normal", width=25, height=5, command=matriz)
    boton_modo_normal.place(x=670, y=250)

    


    
ventanaInicio()
