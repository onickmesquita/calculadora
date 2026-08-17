import unittest
from services.calculadora_service import CalculadoraService

class TestCalculadoraService(unittest.TestCase):
    def setUp(self):
        """Instancia o serviço antes de cada teste."""
        self.service = CalculadoraService()

    def test_soma(self):
        self.assertEqual(self.service.somar(10, 5), 15)
        self.assertEqual(self.service.somar(-1, 1), 0)

    def test_subtracao(self):
        self.assertEqual(self.service.subtrair(10, 5), 5)

    def test_multiplicacao(self):
        self.assertEqual(self.service.multiplicar(10, 5), 50)
        self.assertEqual(self.service.multiplicar(10, 0), 0)

    def test_divisao(self):
        self.assertEqual(self.service.dividir(10, 2), 5)
        # Valida se o erro de divisão por zero é lançado [2]
        with self.assertRaises(ZeroDivisionError):
            self.service.dividir(10, 0)

    def test_sistema_memoria(self):
        """Testa M+, M- e a persistência temporária da memória."""
        self.service.memoria_guardar(100)
        self.assertEqual(self.service.memoria, 100)
        
        self.service.memoria_subtrair(30)
        self.assertEqual(self.service.memoria, 70)

    def test_limpeza_total(self):
        """Testa o reset completo do estado (Etapa 7)."""
        self.service.memoria_guardar(50)
        self.service.limpar_tudo()
        self.assertEqual(self.service.memoria, 0.0)

if __name__ == "__main__":
    unittest.main()