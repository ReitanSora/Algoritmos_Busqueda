
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
