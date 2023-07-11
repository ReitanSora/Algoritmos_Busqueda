
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


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def init_widgets(self):

        # titulo de la ventana
        tk.Label(self,
                 text="Bienvenido al programa sobre algoritmos de búsqueda",
                 **style.STYLE_TITTLE,
                 wraplength="700p"
                 ).pack(side=tk.TOP, fill=tk.X, pady=20)

        tk.Label(self,
                 text='''Un algoritmo de búsqueda es aquel que está diseñado para localizar un elemento de ciertas propiedades dentro de una estrucutra de datos
                        ''',
                 **style.STYLE_TEXT,
                 justify="left",
                 wraplength="600p"
                 ).pack(side=tk.TOP, anchor=tk.W, padx=20)
        
        tk.Label(self,
                 text='''En este programa de la materia de algoritmos, se encuentran 4 búsquedas diferentes, como la búsqueda lineal, binaria de forma iterativa, binaria de forma recursiva y la búsqueda hash.
                        ''',
                 **style.STYLE_TEXT,
                 justify="left",
                 wraplength="600p"
                 ).pack(side=tk.TOP, anchor=tk.W, padx=20)
        
        tk.Label(self,
                 text='''Búsqueda Lineal''',
                 **style.STYLE_SUBTITTLE,
                 justify="left",
                 wraplength="600p"
                 ).pack(side=tk.TOP, anchor=tk.W, padx=20)
        
        tk.Label(self,
                 text='''Como dice su nombre, consiste en ir comparando el elemento buscado con cada elemento del array hasta encontrarlo
                        ''',
                 **style.STYLE_TEXT,
                 justify="left",
                 wraplength="600p"
                 ).pack(side=tk.TOP, anchor=tk.W, padx=20)