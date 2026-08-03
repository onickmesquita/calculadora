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
        
        # Exemplo de botão especializado (SRP aplicado à UI)
        btn_soma = ttk.Button(self.window, text="+", command=self._executar_soma)
        btn_soma.grid(row=1, column=3, sticky="nsew")
        
        
    def _executar_soma(self):
        # A interface apenas captura dados e delega o cálculo ao serviço
        pass
    
    
    def run(self):
        self.window.mainloop()