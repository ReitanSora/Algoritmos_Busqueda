
# Tema: Algoritmos de búsqueda
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI4 - 002
# Fecha de entrega: 12/07/2023

import tkinter as tk
from functions import events as event
from static import style


class Navegacion(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.init_widgets(parent)

    def init_widgets(self, parent):
        nav_frame = tk.Frame(parent)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        nav_frame.configure(background=style.COLOR_CIAN_CLARO, borderwidth=0)

        boton_inicio = tk.Button(nav_frame,
                                 text="Inicio",
                                 **style.STYLE_BUTTON_NAV,
                                 command=parent.move_to_home,
                                 )
        boton_inicio.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        boton_inicio.bind('<Enter>', event.on_enter_nav)
        boton_inicio.bind('<Leave>', event.on_leave_nav)

        boton_errores = tk.Button(nav_frame,
                                  text="Búsquedas",
                                  **style.STYLE_BUTTON_NAV,
                                  command=parent.move_to_busquedas,
                                  )
        boton_errores.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        boton_errores.bind('<Enter>', event.on_enter_nav)
        boton_errores.bind('<Leave>', event.on_leave_nav)

        # label de información - footer
        tk.Label(nav_frame,
                 text="Programa sobre Búsquedas\nGrupo-3",
                 font=("Corbel", 10, "normal"),
                 background=style.COLOR_CIAN_CLARO,
                 foreground="#FFF",
                 justify="center"
                 ).pack(side=tk.BOTTOM, fill=tk.BOTH)
