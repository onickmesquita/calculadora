import tkinter as tk
from tkinter import ttk

class CalculadoraGUI:
    
    
    def __init__(self, service):
        self.service = service  # Injeção da lógica de cálculos
        self.window = tk.Tk()
        self.window.title("Calculadora Python")
        self._configurar_layout()
        
        
    def _configurar_layout(self):
        # Display de entrada de dados
        self.display = ttk.Entry(self.window, font=("Arial", 24), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Matriz de botões: (texto, linha, coluna)
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ] 
        
        # Criação dinâmica para manter o código limpo e evitarmos repetições
        for (texto, linha, coluna) in botoes:
            # Usamos ttk.Button para um visual moderno
            btn = ttk.Button(self.window, text=texto, command=lambda t=texto: self._ao_clicar(t))
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)
        
        
    def _ao_clicar(self, valor):
        # Método centralizador para processar a entrada
        print(f"Botão {valor} clicado")
        
        
    def _executar_soma(self):
        # A interface apenas captura dados e delega o cálculo ao serviço
        pass
    
    
    def run(self):
        self.window.mainloop()