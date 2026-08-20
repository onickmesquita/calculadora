class CalculadoraService:

    """
    Classe especializada em operações matemáticas.
    sua única responsabilidade é realizar cálculos.
    """
    def __init__(self):
        self.memoria = 0.0  # Estado inicial da memória


    def somar(self, num1: float, num2: float) -> float:
        return num1 + num2


    def subtrair(self, num1: float, num2: float) -> float:
        return num1 - num2


    def multiplicar(self, num1: float, num2: float) -> float:
        return num1 * num2


    def dividir(self, num1: float, num2: float) -> float:
        if num2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return num1 / num2
    
    
    def limpar_tudo(self):
        """Reseta o estado interno da calculadora."""
        self.memoria = 0.0
    
    
    def memoria_guardar(self, valor: float):
        """M+: Adiciona o valor atual à memória."""
        self.memoria += valor
        
        
    def memoria_subtrair(self, valor: float):
        """M-: Subtrai o valor atual da memória."""
        self.memoria -= valor     