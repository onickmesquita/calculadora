import tkinter as tk
from tkinter import ttk

def aplicar_estilos():
    # Estilo para o display
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", font=("Arial", 14), padding=10)
    # Adicione aqui todas as configurações de cores e fontes
    return {
        "bg_janela": "#2c3e50",
        "bg_display": "#34495e",
        "fg_display": "white",
        "cor_operador": "#e67e22",
        "cor_numero": "#ecf0f1",
        "fonte_display": ("Arial", 28),
        "fonte_botao": ("Arial", 14, "bold")
    }
    
