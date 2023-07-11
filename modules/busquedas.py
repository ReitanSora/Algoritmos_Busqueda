
# Tema: Algoritmos de búsqueda
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI4 - 002
# Fecha de entrega: 12/07/2023

import tkinter as tk
import random as r
import time
from static import style
from functions import events as event
from functions import busquedas


class AlgoritmosBusqueda(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.matriz = list()
        self.busqueda = tk.IntVar(value=1)
        self.init_widget()

    def vaciar_campos(self):
        self.valor_ingresado.set("")
        self.valor_ordenado.set("")
        self.valor_buscado.set("")
        self.respuesta.set("")
        self.texto_alerta_numero_ingresado.set("")
        self.texto_alerta_numero_buscado.set("")
        self.mensaje.set("")
        self.matriz.clear()

    def aleatorio(self):
        aux = r.randint(-1000, 1000)
        self.matriz.append(aux)
        self.matriz = busquedas.quicksort(self.matriz)
        self.valor_ordenado.set(str(self.matriz).replace("  ", ",")[1:-1])

    def ingresar(self):
        try:
            aux = int(self.valor_ingresado.get())
            self.matriz.append(aux)
            self.texto_alerta_numero_ingresado.set("")
            self.matriz = busquedas.quicksort(self.matriz)
            self.valor_ordenado.set(str(self.matriz).replace("  ", ",")[1:-1])
        except ValueError:
            self.texto_alerta_numero_ingresado.set(
                "Ingrese un número correcto")

    def buscar(self):
        try:
            aux = int(self.valor_buscado.get())
            self.texto_alerta_numero_buscado.set("")
            inicio = time.time()
            if self.busqueda.get() == 1:
                busquedas.busqueda_lineal(self.matriz, aux)
                posicion = busquedas.busqueda_lineal(self.matriz, aux)
                fin = time.time()
                tiempo_final = fin - inicio
                self.mensaje.set("El tiempo de ejecución de la búsqueda fue: {:.6f} s en buscar el número [{}] en un arreglo de [{}] elementos, usando el Algoritmo de Búsqueda {}".format(
                    tiempo_final, aux, len(self.matriz), "Lineal"))
                self.respuesta.set("El número [{}] se encuentra en la posición [{}]".format(
                    aux, posicion) if posicion != -1 else "No se encontró el valor en el arreglo")
                
            elif self.busqueda.get() == 2:
                busquedas.busqueda_binaria(self.matriz, aux)
                posicion = busquedas.busqueda_binaria(self.matriz, aux)
                fin = time.time()
                tiempo_final = fin - inicio
                self.mensaje.set("El tiempo de ejecución de la búsqueda fue: {:.6f} s en buscar el número [{}] en un arreglo de [{}] elementos, usando el Algoritmo de Búsqueda {}".format(
                    tiempo_final, aux, len(self.matriz), "Binaria Iterativa"))
                self.respuesta.set("El número [{}] se encuentra en la posición [{}]".format(
                    aux, posicion) if posicion != -1 else "No se encontró el valor en el arreglo")
            
            elif self.busqueda.get() ==3:
                pass
                # busquedas.binaria_r(self.matriz, aux)
                # posicion = busquedas.binaria_r(self.matriz, aux)
                # fin = time.time()
                # tiempo_final = fin - inicio
                # self.mensaje.set("El tiempo de ejecución de la búsqueda fue: {:.6f} s en buscar el número [{}] en un arreglo de [{}] elementos, usando el Algoritmo de Búsqueda {}".format(
                #     tiempo_final, aux, len(self.matriz), "Binaria Recursiva"))
                # self.respuesta.set("El número [{}] se encuentra en la posición [{}]".format(
                #     aux, posicion) if posicion != -1 else "No se encontró el valor en el arreglo")
                
            elif self.busqueda.get() == 4:
                busquedas.busqueda_hash(self.matriz, aux)
                posicion = busquedas.busqueda_hash(self.matriz, aux)
                fin = time.time()
                tiempo_final = fin - inicio
                self.texto_alerta_numero_buscado.set("")
                self.mensaje.set("El tiempo de ejecución de la búsqueda fue: {:.6f} s en buscar el número [{}] en un arreglo de [{}] elementos, usando el Algoritmo de Búsqueda {}".format(
                    tiempo_final, aux, len(self.matriz), "Hash"))
                self.respuesta.set("El número [{}] se encuentra en la posición [{}]".format(
                    aux, posicion) if posicion != -1 else "No se encontró el valor en el arreglo")
        except ValueError:
            self.texto_alerta_numero_buscado.set("Ingrese un número correcto")

    def init_widget(self):
        # titulo de la ventana
        tk.Label(self,
                 text="Búsqueda Lineal",
                 **style.STYLE_TITTLE,
                 ).pack(side=tk.TOP, fill=tk.X, pady=20)

        # frame donde se colocará toda la información que ingrese el usuario y botones
        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=2)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # label del ingreso de numeros
        tk.Label(input_frame,
                 text="Ingrese un número",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=0, column=0, pady=20, padx=20)

        # label del array ordenado
        tk.Label(input_frame,
                 text="Números ordenados",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=1, column=0, pady=20, padx=20)

        # label del numero a buscar
        tk.Label(input_frame,
                 text="Número a buscar",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=2, column=0, pady=20, padx=20)

        # label de la posicion del numero buscado
        tk.Label(input_frame,
                 text="Ubicación de la búsqueda",
                 **style.STYLE_SUBTITTLE
                 ).grid(row=3, column=0, pady=20, padx=20)

        # entry para los numeros que ingresa el usuario
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, columnspan=2, pady=20, padx=20)

        # variable de control para el entry
        self.valor_ingresado = tk.StringVar()
        tk.Entry(borde_entry_1,
                 textvariable=self.valor_ingresado,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        # linea recta que se coloca debajo del entry para mejor apariencia
        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=200)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 200, 0, **style.STYLE_CANVAS_LINE)

        # label alerta del numero ingresado por el usuario
        self.texto_alerta_numero_ingresado = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_numero_ingresado,
                 **style.STYLE_WARNING
                 ).pack()

        # entry para los numeros ordenados
        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=1, column=1, columnspan=2,
                           pady=20, padx=20, sticky=tk.EW)

        # variable de control para el entry
        self.valor_ordenado = tk.StringVar()
        tk.Entry(borde_entry_2,
                 textvariable=self.valor_ordenado,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)

        # linea recta que se coloca debajo del entry para mejor apariencia
        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=350)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 350, 0, **style.STYLE_CANVAS_LINE)

        # entry para el numero que se quiere buscar
        borde_entry_3 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=2, column=1, columnspan=2, pady=20, padx=20)

        # variable de control para el entry
        self.valor_buscado = tk.StringVar()
        tk.Entry(borde_entry_3,
                 textvariable=self.valor_buscado,
                 **style.STYLE_ENTRY,
                 ).pack(side=tk.TOP, expand=True)

        # linea recta que se coloca debajo del entry para mejor apariencia
        canvas_linea_3 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=200)
        canvas_linea_3.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_3.create_line(0, 0, 200, 0, **style.STYLE_CANVAS_LINE)

        # label alerta del numero ingresado por el usuario
        self.texto_alerta_numero_buscado = tk.StringVar()
        tk.Label(borde_entry_3,
                 textvariable=self.texto_alerta_numero_buscado,
                 **style.STYLE_WARNING
                 ).pack()

        # entry para la respuesta de la posicion de lo que queremos buscar
        borde_entry_4 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=3, column=1, columnspan=2,
                           pady=20, padx=20, sticky=tk.EW)

        # variable de control para el entry
        self.respuesta = tk.StringVar()
        tk.Entry(borde_entry_4,
                 textvariable=self.respuesta,
                 **style.STYLE_ENTRY_DES,
                 ).pack(side=tk.TOP, fill=tk.X, expand=True)

        # linea recta que se coloca debajo del entry para mejor apariencia
        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=350)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(0, 0, 350, 0, **style.STYLE_CANVAS_LINE)

        # boton para ingresar un numero
        borde_1 = tk.LabelFrame(input_frame, **style.STYLE_BUTTON_BORDER)
        borde_1.grid(row=0, column=3, pady=20, padx=20)

        boton_calculo = tk.Button(borde_1,
                                  text="Ingresar",
                                  **style.STYLE_BUTTON,
                                  command=self.ingresar,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        # boton aleatorio
        borde_2 = tk.LabelFrame(input_frame, **style.STYLE_BUTTON_BORDER)
        borde_2.grid(row=1, column=3, pady=20, padx=20)

        boton_aleatorio = tk.Button(borde_2,
                                    text="Aleatorio",
                                    **style.STYLE_BUTTON,
                                    command=self.aleatorio,
                                    )
        boton_aleatorio.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_aleatorio.bind('<Enter>', event.on_enter)
        boton_aleatorio.bind('<Leave>', event.on_leave)

        # boton buscar
        borde_3 = tk.LabelFrame(input_frame, **style.STYLE_BUTTON_BORDER)
        borde_3.grid(row=2, column=3, pady=20, padx=20)

        boton_buscar = tk.Button(borde_3,
                                 text="Buscar",
                                 **style.STYLE_BUTTON,
                                 command=self.buscar,
                                 )
        boton_buscar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_buscar.bind('<Enter>', event.on_enter)
        boton_buscar.bind('<Leave>', event.on_leave)

        # boton vaciar campos
        borde_4 = tk.LabelFrame(input_frame, **style.STYLE_BUTTON_BORDER)
        borde_4.grid(row=3, column=3, pady=20, padx=20)

        boton_vaciar = tk.Button(borde_4,
                                 text="Vaciar Campos",
                                 **style.STYLE_BUTTON,
                                 command=self.vaciar_campos,
                                 )
        boton_vaciar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_vaciar.bind('<Enter>', event.on_enter)
        boton_vaciar.bind('<Leave>', event.on_leave)

        BUSQUEDAS = {
            "Lineal": 1,
            "Binaria Iterativa": 2,
            "Binaria Recursiva": 3,
            "Hash": 4
        }

        borde_seleccion_1 = tk.LabelFrame(
            input_frame, text="Búsqueda", **style.STYLE_ENTRY_BORDER)
        borde_seleccion_1.grid(
            row=4, column=0, columnspan=4, padx=(40,0), pady=10, sticky=tk.NSEW)

        for keys, values in BUSQUEDAS.items():
            tk.Radiobutton(borde_seleccion_1,
                           text=keys,
                           value=values,
                           variable=self.busqueda,
                           **style.STYLE_RADIO_BUTTON,
                           ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=5)

        # area de texto para mostrar información al usuario
        self.mensaje = tk.StringVar()
        tk.Label(self,
                 textvariable=self.mensaje,
                 **style.STYLE_TEXT_AREA,
                 ).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
