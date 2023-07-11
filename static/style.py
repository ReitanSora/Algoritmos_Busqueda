
# Tema: Algoritmos de búsqueda
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI4 - 002
# Fecha de entrega: 12/07/2023

BG = "#3E2929"

COLOR_TITULO = "#FEFFEA"
COLOR_SUBTITULO = "#FEFFEA"

COLOR_BLANCO = "#FFF"
COLOR_NEGRO = "#000"
COLOR_GRIS = "#C2C2C2"
COLOR_AQUA = "#257dca"
COLOR_AQUA_OSCURO = "#1D6AAD"
COLOR_MAGENTA_NORMAL = "#512BCF"
COLOR_MAGENTA_CLARO = "#8A67FF"
COLOR_MAGENTA_OSCURO = "#3b1f98"
COLOR_CIAN_CLARO = "#FF6B6B"
COLOR_CIAN_NORMAL = "#CA2525"
COLOR_CIAN_OSCURO = "#AD1D1D"


STYLE_TITTLE = {
    "font": ("Corbel", 20, "bold"),
    "bg": BG,
    "fg": COLOR_TITULO
}

STYLE_SUBTITTLE = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_SUBTITULO,
}

STYLE_TEXT = {
    "font": ("Corbel", 14, ""),
    "bg": BG,
    "fg": COLOR_SUBTITULO,
}

STYLE_WARNING = {
    "font": ("Corbel", 9, "bold"),
    "bg": BG,
    "fg": COLOR_GRIS,
}

STYLE_ENTRY_BORDER = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_GRIS,
    "bd": 0,
    "relief": "flat",
}

STYLE_BUTTON_BORDER = {
    "bg": COLOR_CIAN_CLARO,
    "relief": "flat",
    "bd": 3,
    "width": 12,
}

STYLE_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": COLOR_BLANCO,
    "fg": COLOR_CIAN_CLARO,
    "activeforeground": COLOR_CIAN_CLARO,
    "activebackground": COLOR_BLANCO,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "padx": 20,
}

STYLE_BUTTON_NAV = {
    "font": ("Corbel", 14, "bold"),
    "bg": COLOR_CIAN_CLARO,
    "fg": COLOR_BLANCO,
    "activeforeground": COLOR_CIAN_CLARO,
    "activebackground": COLOR_BLANCO,
    "relief": "sunken",
    "cursor": "hand2",
    "bd": 0,
    "width": 10,
    "height": 3,
    "padx": 20,
}

STYLE_BUTTON_ENTER = {
    "bg": COLOR_CIAN_CLARO,
    "fg": COLOR_BLANCO,
}

STYLE_BUTTON_NAV_ENTER = {
    "bg": COLOR_CIAN_NORMAL,
    "fg": COLOR_BLANCO
}

STYLE_ENTRY = {
    "font": ("Verdana", 14),
    "bg": BG,
    "fg": COLOR_TITULO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_CIAN_CLARO,
    "justify": "center"
}

STYLE_ENTRY_DES = {
    "font": ("Verdana", 10),
    "fg": COLOR_BLANCO,
    "bd": 0,
    "selectbackground": COLOR_BLANCO,
    "selectforeground": COLOR_CIAN_CLARO,
    "readonlybackground": BG,
    "cursor": "",
    "state": "readonly",
    "justify": "center"
}

STYLE_CANVAS = {
    "bg": BG,
    "height": 3,
    "bd": 0,
    "relief": "flat",
    "highlightthickness": 0
}

STYLE_CANVAS_LINE = {
    "width": "3",
    "fill": COLOR_CIAN_CLARO
}

STYLE_TEXT_AREA = {
    "font": ("Verdana", 12),
    "background": BG,
    "foreground": COLOR_GRIS,
    "bd": 0,
    "cursor": "",
    "state": "disable",
    "justify": "left",
    "wraplength": "600p"
}

STYLE_RADIO_BUTTON = {
    "font": ("Corbel", 14, "bold"),
    "bg": BG,
    "fg": COLOR_BLANCO,
    "activebackground": BG,
    "activeforeground": COLOR_MAGENTA_CLARO,
    "selectcolor": BG,
    "border": "0",
    "anchor": "center",
    "borderwidth": "0",
    "relief": "flat"
}
