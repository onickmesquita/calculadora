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
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('M+', 5, 0), ('M-', 5, 1)
        ] 
        
        # Criação dinâmica para manter o código limpo e evitarmos repetições
        for (texto, linha, coluna) in botoes:
            # Usamos ttk.Button para um visual moderno
            btn = ttk.Button(self.window, text=texto, command=lambda t=texto: self._ao_clicar(t))
            btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)
        
        
    def _ao_clicar(self, valor):
        operadores = ('+', '-', '*', '/')
        texto_atual = self.display.get()
        
        # Se clicar em 'C', limpa o display.
        if valor == 'C':
            self.display.delete(0, tk.END)
        
        # Se clicar em '=', deixaremos pronto para a integração (Etapa 5)
        elif valor == '=':
            print("Solicitando cálculo...")
            # Aqui chamaremos o service no próximo passo
        
        elif valor in ('M+', 'M-'):
            self._processar_memoria(valor)
        
        # Etapa 8: Bloqueia clique duplo em operadores
        elif valor in operadores and texto_atual.endswith(operadores):
            # Substitui o operador anterior pelo novo ou apenas ignora
            self.display.delete(len(texto_atual)-1, tk.END)
            self.display.insert(tk.END, valor)
            
        # Para números e operadores, apenas adicionamos ao final do texto atual
        else:
            self.display.insert(tk.END, valor)
    
    
    def _processar_memoria(self, acao):
        try:
            valor_atual = float(self.display.get())
            if acao == 'M+':
                self.service.memoria_guardar(valor_atual)
            else:
                self.service.memoria_subtrair(valor_atual)
            self.display.delete(0, tk.END) # Limpa após guardar
        except ValueError:
            self.display.insert(tk.END, "Erro")
    
    
    def _executar_calculo(self):
        try:
            # Obtém a expressão do display
            expressao = self.display.get()
            if not expressao:
                return
            
            # Para fins didáticos nesta etapa, usaremos eval() para processar a string,
            # mas o ideal é que seu service contenha as regras de parsing futuramente.
            resultado = eval(expressao)
            
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(resultado))
            
            
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro: Divisão por 0")
        except SyntaxError:
             # Captura expressões incompletas ou malformadas
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro: Operação Inválida")
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Entrada Inválida")
        
        
    def _executar_soma(self):
        # A interface apenas captura dados e delega o cálculo ao serviço
        pass
    
    
    def run(self):
        self.window.mainloop()