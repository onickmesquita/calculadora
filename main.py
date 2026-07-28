from services.calculadora_service import CalculadoraService
# Futuramente importaremos a interface aqui:
# from ui.calculadora_gui import CalculadoraGUI

def main():
    # Instanciamos o serviço (Lógica de Negócio).
    servico = CalculadoraService()
    
    print("Calculadora Iniciada com Sucesso!")
    # O próximo passo será passar esse 'servico' para a nossa interface.
    # app = CalculadoraGUI(servico)
    # app.run()
    
if __name__ == "__main__":
    # Uso idiomático para garantir que o script só rode se executado diretamente.
    main()