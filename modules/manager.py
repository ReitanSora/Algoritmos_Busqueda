
# Tema: Algoritmos de búsqueda
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI4 - 002
# Fecha de entrega: 12/07/2023

import tkinter as tk
from static import style
from modules.navegacion import Navegacion
from modules.home import Home
from modules.busquedas import AlgoritmosBusqueda


class Manager(tk.Tk):

    def __init__(self, *args, **kwargs):
        # metodo constructor de la clase Tk
        super().__init__(*args, **kwargs)
        self.title("Algoritmos")
        self.geometry("1000x600")
        self.resizable(False, False)
        # self.overrideredirect(True)

        # contenedor para los botones de navegacion
        Navegacion(self)

        # contenedor donde se mostrarán todas las demás ventanas
        container = tk.Frame(self)
        container.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BG, bd=0)
        container.config(width="800")

        # creacion de filas y clumnas disponibles en el frame container,
        # 0 = 1 columna/fila ; weight = espacio que ocupa
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # diccionario de clases
        self.frames = {}

        for F in (Home, AlgoritmosBusqueda):
            frame = F(container, self)
            self.frames[F] = frame

            # configuracion de filas, columnas y rellenado del frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    # metodo para mostrar las diferentes ventanas
    def show_frame(self, container):
        frame = self.frames[container]

        # para poner una pantalla encima de la otra
        frame.tkraise()

    def move_to_home(self):
        self.show_frame(Home)

    def move_to_busquedas(self):
        self.show_frame(AlgoritmosBusqueda)
