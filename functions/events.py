
#Tema: Algoritmos de búsqueda
#Grupo #3
#Integrantes:
#- Stiven Pilca           CI: 1750450262
#- Tulcanza Juan          CI: 1755962485
#Ingeniería en Sistemas de la información
#Paralelo: SI4 - 002
#Fecha de entrega: 12/07/2023

from static import style

# eventos para efecto de hover en botones
def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


def on_enter_return(e):
    e.widget.config(**style.STYLE_BUTTON_RETURN_ENTER)


def on_leave_return(e):
    e.widget.config(**style.STYLE_BUTTON_RETURN)


def on_enter_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV_ENTER)


def on_leave_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV)