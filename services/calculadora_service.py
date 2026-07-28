class CalculadoraService:

    """
    Classe especializada em operações matemáticas.
    sua única responsabilidade é realizar cálculos.
    """

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
    
    