import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog 
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps  
import random
import os
import time


"""
Nombre: ventanaInicio
Entrada: Ninguna
Salida: Crea y muestra la ventana inicial del juego en pantalla completa
Restricciones: Ninguna
"""
def ventanaInicio():

    global root

    root = tk.Tk() 
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.resizable(False, False)
    root.title("Tectris")

    cargarImagenes()

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


"""
Nombre: ventanaPrincipal
Entrada: Evento (e) 
Salida: Muestra la ventana principal del juego con sus botones
Restricciones: Se llama al presionar Enter en la ventana inicial
"""
def ventanaPrincipal(e):

    imagenFondo = Image.open(r"C:/Users/geyer/OneDrive/Escritorio/TEC/Progra/semestre3/taller/Proyecto#2/fondo.jpg")
    fondoPrincipal = ImageTk.PhotoImage(imagenFondo)

    labelFondoPrincipal = tk.Label(root, bg="black")
    labelFondoPrincipal.place(x=0, y=0, relwidth=1, relheight=1)

    botonModoNormal = Button(root, text="Modo Normal", width=25, height=5, command=matriz)
    botonModoNormal.place(x=670, y=250)

    botonCargarPartida = Button(root, text="Cargar partida", width=25, height=5, command=lambda: [matriz(), cargarPartida()])
    botonCargarPartida.place(x=670, y=350)
    


global piezaActual, posicionActual, puntajeTotal, enJuego, menuPausa, menuVisible, enPausa


menuPausa = None
menuVisible = False
enPausa = False
enJuego = False
piezaActual = None
posicionActual = (0, 5)  
rotaciones = {pieza: 0 for pieza in ["O", "I", "L", "J", "T", "Z", "U", "X"]}
puntajeTotal = 0


formas = {
    "O": [(0,0), (0,1), (1,0), (1,1)],
    "I": [(0,0), (1,0), (2,0), (3,0)],
    "L": [(0,0), (1,0), (2,0), (2,1)],
    "J": [(0,1), (1,1), (2,1), (2,0)],
    "T": [(0,0), (0,1), (0,2), (1,1)],
    "Z": [(0,0), (0,1), (1,1), (1,2)],
    "U": [(0,0), (1,0), (1,1), (1,2), (0,2)],
    "X": [(0,1), (1,0), (1,1), (1,2), (2,1)],
    }


pivotes = {
    "O": (0.5, 0.5),  
    "I": (1.5, 0.5),
    "L": (1, 1),
    "J": (1, 1),
    "T": (1, 1),
    "Z": (1, 1),
    "U": (1, 1),
    "X": (1, 1),
}


formaActual = []


"""
Nombre: cargarImagenes
Entrada: Ninguna
Salida: Carga y almacena todas las imágenes necesarias para el juego
Restricciones: Las rutas de las imágenes deben ser válidas
"""
def cargarImagenes():

    global imagenes

    imagenes = {}
    
    imagenes["borde"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\borde.png").resize((30, 30)))
    imagenes["O"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueAmarillo.png").resize((30, 30)))
    imagenes["I"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueAzul.png").resize((30, 30)))
    imagenes["L"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueMorado.png").resize((30, 30)))
    imagenes["J"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueNaranja.png").resize((30, 30)))
    imagenes["T"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueRojo.png").resize((30, 30)))
    imagenes["Z"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueRosado.png").resize((30, 30)))
    imagenes["U"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueVerde.png").resize((30, 30)))
    imagenes["X"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\bloqueVerdeClaro.png").resize((30, 30)))
    imagenes["celdas"] = ImageTk.PhotoImage(Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\fondoCeldas.png").resize((30, 30)))


global celdas
celdas = {}


"""
Nombre: matriz
Entrada: Ninguna
Salida: Crea la matriz del juego y configura la interfaz gráfica
Restricciones: Requiere que las imágenes estén cargadas previamente
"""
def matriz():
    global valores, celdas, labelPuntaje, frameSiguiente
    valores = {}
    celdas = {}

    fondoJuego = Image.open(r"C:\Users\geyer\OneDrive\Escritorio\TEC\Progra\semestre3\taller\Proyecto#2\marcoJuego.png")
    fondoJuego = fondoJuego.resize((525, 669))
    fondoJuegoImg = ImageTk.PhotoImage(fondoJuego)
    labelFondoJuego = tk.Label(root, bg="black", image=fondoJuegoImg)
    labelFondoJuego.image = fondoJuegoImg  
    labelFondoJuego.place(x=0, y=0, relwidth=1, relheight=1)

    frameTablero = tk.LabelFrame(root, bg="black", bd=0)
    frameTablero.place(x=528, y=97)  

    for fila in range(22):
        for columna in range(12):
            label = tk.Label(frameTablero, bd=0)
            label.grid(row=fila, column=columna)
            celdas[(fila, columna)] = label
            if (columna == 0) or (columna == 11) or (fila == 0) or (fila == 21):
                valores[(fila, columna)] = "+"
                label.config(image=imagenes["borde"])
                label.image = imagenes["borde"]
            else:
                valores[(fila, columna)] = 0
                label.config(image=imagenes["celdas"])
                label.image = imagenes["celdas"]

    labelPuntaje = tk.Label(root, text="Puntaje: 0", font=("Arial", 14), bg="black", fg="white")
    labelPuntaje.place(x=900, y=518)

    configurarControles()
    iniciarJuego()


"""
Nombre: generarPieza
Entrada: Ninguna
Salida: Retorna un tetronimo aleatorio (O, I, L, J, T, Z, U, X)
Restricciones: Ninguna
"""
def generarPieza():
    piezas = ["O", "I", "L", "J", "T", "Z", "U", "X"]
    return random.choice(piezas)


"""
Nombre: ponerPiezas
Entrada: pieza (str), fila (int), columna (int)
Salida: Coloca una pieza en la posición especificada del tablero
Restricciones: Las coordenadas deben estar dentro del tablero
"""
def ponerPiezas(pieza, fila, columna):
    global valores
    forma = formas[pieza]
    
    for x1, y1 in forma:
        x2, y2 = fila + x1, columna + y1
        if 0 <= x2 < 22 and 0 <= y2 < 12:
            valores[(x2, y2)] = 1
            img = ImageTk.PhotoImage(imagenes[pieza])
            celdas[(x2, y2)].config(image=img)
            celdas[(x2, y2)].image = img  


"""
Nombre: moverPieza
Entrada: direccion - 'izquierda', 'derecha' o 'abajo'
Salida: Mueve la pieza actual en la dirección especificada si es posible
Restricciones: La dirección debe ser válida
"""
def moverPieza(direccion):
    global posicionActual
    
    if direccion == 'abajo':
        nuevaPos = (posicionActual[0] + 1, posicionActual[1])
    elif direccion == 'izquierda':
        nuevaPos = (posicionActual[0], posicionActual[1] - 1)
    elif direccion == 'derecha':
        nuevaPos = (posicionActual[0], posicionActual[1] + 1)
    else:
        return False
    
    if not verificarColision(nuevaPos):
        posicionActual = nuevaPos
        actualizarTablero()
        return True
    return False


"""
Nombre: nuevaPosicionPieza
Entrada: posicion, direccion 
Salida: Calcula la nueva posición basada en la dirección de movimiento
Restricciones: La dirección debe ser válida
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
Nombre: rotarForma
Entrada: forma , pivote 
Salida: Retorna la forma rotada 90° en sentido horario alrededor del pivote
Restricciones: Ninguna
"""
def rotarForma(forma, pivote):
    nueva = []
    cx, cy = pivote

    for x, y in forma:
        dx = x - cx
        dy = y - cy

        x_rot = round(cx - dy)
        y_rot = round(cy + dx)

        nueva.append((x_rot, y_rot))

    return nueva


"""
Nombre: rotarPieza
Entrada: Ninguna
Salida: Rota la pieza actual si es posible
Restricciones: Ninguna
"""
def rotarPieza():
    global formaActual, posicionActual, piezaActual

    pivote = pivotes[piezaActual]
    nuevaForma = rotarForma(formaActual, pivote)

    if not verificarColisionForma(nuevaForma, posicionActual):
        formaActual = nuevaForma
        actualizarTablero()
    else:
        intentarAjustesRotacion(nuevaForma)


"""
Nombre: intentarAjustesRotacion
Entrada: nuevaForma 
Salida: Intenta ajustar la posición para permitir la rotación
Restricciones: Ninguna
"""
def intentarAjustesRotacion(nuevaForma):
    global formaActual, posicionActual
    
    ajustes = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
    
    for dx, dy in ajustes:
        nueva_pos = (posicionActual[0] + dx, posicionActual[1] + dy)
        if not verificarColisionForma(nuevaForma, nueva_pos):
            posicionActual = nueva_pos
            formaActual = nuevaForma
            actualizarTablero()
            return


"""
Nombre: verificarColisionForma
Entrada: forma , pos 
Salida: Retorna True si hay colisión con la forma en la posición dada
Restricciones: Ninguna
"""
def verificarColisionForma(forma, pos):
    x, y = pos
    for dx, dy in forma:
        fila = x + dx
        col = y + dy
        if not (0 <= fila < 22 and 0 <= col < 12):
            return True
        valor = valores.get((fila, col), "+")
        if valor != 0 or valor == "+":
            return True
    return False


"""
Nombre: verificarColision
Entrada: pos 
Salida: Retorna True si hay colisión en la posición dada
Restricciones: Ninguna
"""
def verificarColision(pos):
    x, y = pos
    for dx, dy in formaActual:
        fila = x + dx
        col = y + dy
          
        if col <= 0 or col >= 11:  
            return True
        if fila >= 21:  
            return True
            
        if 1 <= fila < 21 and 1 <= col < 11:
            valor = valores.get((fila, col), 0)
            if valor != 0:
                return True
                
    return False


"""
Nombre: configurarControles
Entrada: Ninguna
Salida: Configura los controles del teclado para el juego
Restricciones: Ninguna
"""
def configurarControles():
    root.bind('<Left>', lambda e: moverPieza('izquierda'))
    root.bind('<Right>', lambda e: moverPieza('derecha'))
    root.bind('<Down>', lambda e: moverPieza('abajo'))
    root.bind('<Up>', lambda e: rotarPieza())
    root.bind('<space>', lambda e: colocarPieza())


"""
Nombre: actualizarTablero
Entrada: Ninguna
Salida: Actualiza la interfaz gráfica del tablero
Restricciones: Ninguna
"""
def actualizarTablero():
    
    for fila in range(1, 21):
        for col in range(1, 11):
            valor = valores.get((fila, col), 0)
            if valor == 0:
                celdas[(fila, col)].config(image=imagenes["celdas"])
            elif valor in imagenes:
                celdas[(fila, col)].config(image=imagenes[valor])

    for dy, dx in formaActual:
        y = posicionActual[0] + dy
        x = posicionActual[1] + dx
        if 1 <= y <= 20 and 1 <= x <= 10:
            celdas[(y, x)].config(image=imagenes[piezaActual])


"""
Nombre: colocarPieza
Entrada: Ninguna
Salida: Fija la pieza actual en el tablero y genera una nueva pieza
Restricciones: Ninguna
"""
def colocarPieza():
    global piezaActual, posicionActual, enJuego, formaActual
    
    for dx, dy in formaActual:
        fila = posicionActual[0] + dx
        col = posicionActual[1] + dy
        if 1 <= fila < 21 and 1 <= col < 11:
            valores[(fila, col)] = piezaActual
            celdas[(fila, col)].config(image=imagenes[piezaActual])
    
    eliminarLineasCompletas()
    
    piezaActual = generarPieza()
    formaActual = formas[piezaActual]
    posicionActual = (1, 5)
    
    if verificarColision(posicionActual):
        gameOver()
    else:
        actualizarTablero()


"""
Nombre: verificarColisionInicial
Entrada: Ninguna
Salida: Verifica si hay colisión en la posición inicial de una nueva pieza
Restricciones: Ninguna
"""
def verificarColisionInicial():
    x, y = posicionActual
    for dx, dy in formaActual:  
        nx, ny = x + dx, y + dy
        if valores.get((nx, ny), 0) != 0 and valores.get((nx, ny)) != "+":
            return True
    return False


"""
Nombre: verificarLineasCompletas
Entrada: Ninguna
Salida: Verifica y elimina líneas completas, actualizando el puntaje
Restricciones: Ninguna
"""
def verificarLineasCompletas():
    global puntajeTotal
    lineas_completas = 0
    
    for fila in range(1, 21):
        if all(valores[(fila, col)] != 0 for col in range(1, 11)):

            for col in range(1, 11):
                valores[(fila, col)] = 0
                celdas[(f, col)].config(image=celdas[(f-1, col)].image)
            
            for f in range(fila, 1, -1):
                for col in range(1, 11):
                    valores[(f, col)] = valores[(f-1, col)]
                    img = celdas[(f-1, col)].image
                    celdas[(f, col)].config(image=img)
            
            lineas_completas += 1
    
    if lineas_completas > 0:
        puntajeTotal += lineas_completas * 100
        actualizarPuntajeVisual()


"""
Nombre: actualizarPuntajeVisual
Entrada: Ninguna
Salida: Actualiza la visualización del puntaje en pantalla
Restricciones: Ninguna
"""
def actualizarPuntajeVisual():
    
    labelPuntaje.config(text=f"Puntaje: {puntajeTotal}")


"""
Nombre: puntaje
Entrada: fila  
Salida: Retorna 100 puntos por cada fila completada
Restricciones: Ninguna
"""
def puntaje(fila):

    return 100   


"""
Nombre: iniciarJuego
Entrada: Ninguna
Salida: Inicia una nueva partida reiniciando el tablero y variables
Restricciones: Ninguna
"""
def iniciarJuego():
    global piezaActual, posicionActual, enJuego, formaActual, puntajeTotal, valores
    
    puntajeTotal = 0
    labelPuntaje.config(text="Puntaje: 0")

    crearBotones()
    
    for fila in range(22):
        for col in range(12):
            if (col == 0) or (col == 11) or (fila == 0) or (fila == 21):
                valores[(fila, col)] = "+"
                celdas[(fila, col)].config(image=imagenes["borde"])
            else:
                valores[(fila, col)] = 0
                celdas[(fila, col)].config(image=imagenes["celdas"])
    
    piezaActual = generarPieza()
    formaActual = formas[piezaActual]
    posicionActual = (1, 5)  
    
    if verificarColision(posicionActual):
        gameOver()
    else:
        enJuego = True
        actualizarTablero()
        bajarPiezaAutomaticamente()  


"""
Nombre: eliminarLineasCompletas
Entrada: Ninguna
Salida: Elimina líneas completas y actualiza el tablero y puntaje
Restricciones: Ninguna
"""
def eliminarLineasCompletas():
    global puntajeTotal, valores
    
    lineas_eliminadas = 0
    fila = 20  
    
    while fila >= 1:  
        
        if all(valores[(fila, col)] != 0 for col in range(1, 11)):
            lineas_eliminadas += 1
            
            for f in range(fila, 1, -1):
                for col in range(1, 11):
                    valores[(f, col)] = valores[(f-1, col)]
            
            for col in range(1, 11):
                valores[(1, col)] = 0
            
        else:
            fila -= 1  
    
    if lineas_eliminadas > 0:
        puntajeTotal += lineas_eliminadas * 100
        labelPuntaje.config(text=f"Puntaje: {puntajeTotal}")
        
        if lineas_eliminadas > 1:
            bonus = (lineas_eliminadas - 1) * 50
            puntajeTotal += bonus
            mostrarBonus(bonus)
        
        actualizarTableroCompleto()


"""
Nombre: mostrarBonus
Entrada: cantidad 
Salida: Muestra temporalmente el bonus obtenido
Restricciones: Ninguna
"""
def mostrarBonus(cantidad):
    bonus_label = tk.Label(root, text=f"Bonus +{cantidad}!", 
                         font=("Arial", 14), bg="black", fg="yellow")
    bonus_label.place(x=900, y=450)
    root.after(1000, bonus_label.destroy)
    
    def desaparecer():
        bonus_label.destroy()
    
    root.after(1000, desaparecer)        


"""
Nombre: parpadearLineasEliminadas
Entrada: cantidad (int) - número de líneas eliminadas
Salida: Efecto visual de parpadeo para las líneas eliminadas
Restricciones: Ninguna
"""
def parpadearLineasEliminadas(cantidad):
    
    lineas = list(range(20, 20-cantidad, -1))
    
    for _ in range(3):  
        for fila in lineas:
            for col in range(1, 11):
                celdas[(fila, col)].config(image=imagenes["celdas"])
        root.update()
        root.after(100)  
        
        for fila in lineas:
            for col in range(1, 11):
                if valores.get((fila, col), 0) != 0:
                    pieza = valores[(fila, col)]
                    celdas[(fila, col)].config(image=imagenes[pieza])
        root.update()
        root.after(100)


"""
Nombre: bajarPiezaAutomaticamente
Entrada: Ninguna
Salida: Mueve la pieza hacia abajo automáticamente cada cierto tiempo
Restricciones: Ninguna
"""
def bajarPiezaAutomaticamente():
    if enJuego:
        if not moverPieza('abajo'):
            colocarPieza()
        if enJuego:  
            root.after(500, bajarPiezaAutomaticamente)


"""
Nombre: gameOver
Entrada: Ninguna
Salida: Finaliza el juego, muestra el puntaje obtenido y retorna a la ventana principal
Restricciones: Ninguna
"""
def gameOver():
    global enJuego
    enJuego = False
    messagebox.showinfo("Game Over", f"Juego terminado! Puntaje: {puntajeTotal}")
    ventanaPrincipal(None)

"""
Nombre: guardarPartida
Entrada: Ninguna
Salida: Guarda el estado actual del juego en un archivo
Restricciones: Ninguna
"""
def guardarPartida():
    archivo = filedialog.asksaveasfilename(title="Guardar partida", defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")], initialdir="./saves")
    
    if not archivo:
        return
    
    try:
        archivoGuardar = open(archivo, "w")
        
        for fila in range(22):
            for col in range(12):
                archivoGuardar.write(str(valores[(fila, col)]) + " ")
            archivoGuardar.write("\n")
        
        archivoGuardar.write(piezaActual + "\n")
        archivoGuardar.write(str(posicionActual[0]) + " " + str(posicionActual[1]) + "\n")
        archivoGuardar.write(str(puntajeTotal) + "\n")
        
        archivoGuardar.close()
        
        mensaje = "Partida guardada en:\n" + archivo
        messagebox.showinfo("Éxito", mensaje)
    except Exception as e:
        mensajeError = "No se pudo guardar:\n" + str(e)
        messagebox.showerror("Error", mensajeError)


"""
Nombre: cargarPartida
Entrada: Ninguna
Salida: Carga una partida guardada desde un archivo
Restricciones: El archivo debe tener el formato correcto
"""
def cargarPartida():
    global valores, piezaActual, posicionActual, puntajeTotal
    
    archivo = filedialog.askopenfilename(title="Cargar partida", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")], initialdir="./saves")
    
    if not archivo:
        return False
    
    try:
        archivoCargar = open(archivo, "r")
        lineas = archivoCargar.readlines()
        archivoCargar.close()
        
        for fila in range(22):
            partes = lineas[fila].strip().split()
            for col in range(12):
                val = partes[col]
                if val == '+':
                    valores[(fila, col)] = '+'
                elif val.isdigit():
                    valores[(fila, col)] = int(val)
                else:
                    valores[(fila, col)] = val
        
        piezaActual = lineas[22].strip()
        pos_x, pos_y = lineas[23].strip().split()
        posicionActual = (int(pos_x), int(pos_y))
        puntajeTotal = int(lineas[24].strip())
        
        actualizarTableroCompleto()
        labelPuntaje.config(text="Puntaje: " + str(puntajeTotal))
        
        mensaje = "Partida cargada correctamente"
        messagebox.showinfo("Éxito", mensaje)
        return True
    except Exception as e:
        mensaje_error = "Archivo corrupto o incompatible:\n" + str(e)
        messagebox.showerror("Error", mensaje_error)
        return False
    

"""
Nombre: actualizarTableroCompleto
Entrada: Ninguna
Salida: Actualiza toda la interfaz gráfica del tablero
Restricciones: Ninguna
"""
def actualizarTableroCompleto():
    for fila in range(22):
        for col in range(12):
            valor = valores.get((fila, col), 0)
            if valor == '+':
                celdas[(fila, col)].config(image=imagenes["borde"])
            elif valor == 0:
                celdas[(fila, col)].config(image=imagenes["celdas"])
            elif valor in imagenes:
                celdas[(fila, col)].config(image=imagenes[valor])


"""
Nombre: crearBotones
Entrada: Ninguna
Salida: Crea y posiciona los botones de la interfaz
Restricciones: Debe llamarse después de inicializar la ventana principal
"""
def crearBotones():
    # Botón Guardar
    botonGuardar = Button(root, text="Guardar", command=guardarPartida,
                      font=("Arial", 12), bg="#4CAF50", fg="white",
                      width=10, height=1)
    botonGuardar.place(x=900, y=120)
    
    # Botón Cargar
    botonCargar = Button(root, text="Cargar", command=cargarPartida,
                     font=("Arial", 12), bg="#2196F3", fg="white",
                     width=10, height=1)
    botonCargar.place(x=900, y=170)
    
    # Botón Pausa
    botonPausa = Button(root, text="Pausa", command=mostrarMenuPausa,
                    font=("Arial", 12), bg="#FF5722", fg="white",
                    width=10, height=1)
    botonPausa.place(x=900, y=220)
    
    # Botón Salir
    botonSalir = Button(root, text="Salir", command=root.quit,
                    font=("Arial", 12), bg="#F44336", fg="white",
                    width=10, height=1)
    botonSalir.place(x=900, y=270)


"""
Nombre: pausarJuego
Entrada: Ninguna
Salida: Pausa o reanuda el juego
Restricciones: Ninguna
"""
def pausarJuego():
    global enJuego, enPausa
    
    if enJuego:
        enJuego = False
        enPausa = True
    elif enPausa:
        enJuego = True
        enPausa = False
        bajarPiezaAutomaticamente()


"""
Nombre: continuarJuego
Entrada: Ninguna
Salida: Reanuda el juego y cierra el menú de pausa
Restricciones: Debe llamarse cuando el juego está pausado
"""
def continuarJuego():
    global menuPausa, menuVisible, enPausa, enJuego
    
    if menuPausa:
        menuPausa.destroy()
        menuPausa = None
    menuVisible = False
    enPausa = False
    enJuego = True
    bajarPiezaAutomaticamente()


"""
Nombre: mostrarMenuPausa
Entrada: 
Salida: Muestra/oculta el menú de pausa y controla el estado del juego
Restricciones: Requiere las variables globales menuPausa, menuVisible y enPausa
"""
def mostrarMenuPausa():
    global menuPausa, menuVisible, enPausa
    
    if menuVisible:
        
        if menuPausa:
            menuPausa.destroy()
        menuVisible = False
        enPausa = False
        continuarJuego()
    else:
        
        pausarJuego()
        
        menuPausa = Frame(root, bg="#37474F", bd=2, relief=RAISED)
        menuPausa.place(x=900, y=220, width=150)
        
        opciones = [
            ("Continuar", continuarJuego, "#4CAF50"),
            ("Guardar", guardarPartida, "#2196F3"),
            ("Cargar", cargarPartida, "#9C27B0"),
            ("Salir", root.quit, "#F44336")
        ]
        
        for texto, comando, color in opciones:
            btn = Button(menuPausa, text=texto, command=comando,
                       font=("Arial", 10), bg=color, fg="white",
                       width=12, anchor="w")
            btn.pack(fill=X, pady=2, padx=2)
        
        menuVisible = True
        enPausa = True


"""
Nombre: ocultarMenuPausa
Entrada: Ninguna
Salida: Oculta el menú de pausa si está visible
Restricciones: Ninguna
"""
def ocultarMenuPausa():
    global menuPausa, menuVisible
    if menuPausa is not None:
        menuPausa.destroy()
        menuPausa = None
    menuVisible = False
    
    if enPausa:
        pausarJuego()
    
    
ventanaInicio()