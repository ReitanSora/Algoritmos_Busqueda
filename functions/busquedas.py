
#Tema: Algoritmos de búsqueda
#Grupo #3
#Integrantes:
#- Stiven Pilca           CI: 1750450262
#- Tulcanza Juan          CI: 1755962485
#Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
#Fecha de entrega: 12/07/2023


def quicksort(arr:list):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def busqueda_lineal(arreglo, n):
    posicion = None
    for i in range(len(arreglo)):
        if n == arreglo[i]:
            posicion = i + 1
            break
        else:
            posicion = -1
    return posicion

def busqueda_binaria(arreglo, n):
    m = len(arreglo)
    n2 = m - 1
    aux = 0
    x = 0
    desc = False
    
    while aux <= n2:
        x = (n2 + aux) // 2
        if arreglo[x] == n:
            desc = True
            break
        elif n < arreglo[x]:
            n2 = x - 1
        else:
            aux = x + 1
    
    if desc:
        return x + 1
    else:
        return -1

def binaria_r(arreglo, x, y, n):
    if y >= x and x < len(arreglo):
        aux = x + (y - x) // 2
        if arreglo[aux] == n:
            return aux + 1
        if arreglo[aux] > n:
            return binaria_r(arreglo, x, aux - 1, n)
        return binaria_r(arreglo, aux + 1, y, n)
    return -1

def busqueda_hash(arreglo, n):
    hash_table = {}
    
    for i, item in enumerate(arreglo):
        hash_table[item] = i
    
    if n in hash_table:
        return hash_table[n] + 1
    else:
        return -1

# def buscar():
#     elementos_str = entry_elementos.get()
#     elemento_buscar = entry_elemento.get()
#     metodo = combo_metodos.get()

#     elementos = [x.strip() for x in elementos_str.split(',')]

#     elementos_ordenados = quicksort(elementos)

#     if metodo == "Búsqueda Lineal":
#         posicion = busqueda_lineal(elementos_ordenados, elemento_buscar)
#     elif metodo == "Búsqueda Binaria":
#         posicion = busqueda_binaria(elementos_ordenados, elemento_buscar)
#     elif metodo == "Búsqueda Binaria Recursiva":
#         posicion = binaria_r(elementos_ordenados, 0, len(elementos_ordenados) - 1, elemento_buscar)
#     elif metodo == "Búsqueda Hash":
#         posicion = busqueda_hash(elementos_ordenados, elemento_buscar)

#     if posicion != -1:
#         resultado = f"El elemento '{elemento_buscar}' se encuentra en la posición {posicion}"
#     else:
#         resultado = f"El elemento '{elemento_buscar}' no se encuentra en el arreglo"

#     lbl_resultado["text"] = resultado

# # Crear la ventana
# window = tk.Tk()
# window.title("Búsqueda en Arreglo")
# window.geometry("400x250")

# # Etiqueta y campo de entrada para los elementos del arreglo
# lbl_elementos = tk.Label(window, text="Elementos (separados por comas):")
# lbl_elementos.pack()
# entry_elementos = tk.Entry(window)
# entry_elementos.pack()

# # Etiqueta y campo de entrada para el elemento a buscar
# lbl_elemento = tk.Label(window, text="Elemento a buscar:")
# lbl_elemento.pack()
# entry_elemento = tk.Entry(window)
# entry_elemento.pack()

# # Menú desplegable para seleccionar el método de búsqueda
# lbl_metodo = tk.Label(window, text="Método de búsqueda:")
# lbl_metodo.pack()
# combo_metodos = tk.StringVar()
# combo_metodos.set("Búsqueda Lineal")
# dropdown_metodos = tk.OptionMenu(window, combo_metodos, "Búsqueda Lineal", "Búsqueda Binaria", "Búsqueda Binaria Recursiva", "Búsqueda Hash")
# dropdown_metodos.pack()

# # Botón de búsqueda
# btn_buscar = tk.Button(window, text="Buscar", command=buscar)
# btn_buscar.pack()

# # Etiqueta para mostrar el resultado
# lbl_resultado = tk.Label(window, text="")
# lbl_resultado.pack()

# # Ejecutar la interfaz gráfica
# window.mainloop()
