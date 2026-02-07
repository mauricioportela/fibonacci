import unittest

from fibonacci import Fibonacci, gerar_exemplos


class TestFibonacci(unittest.TestCase):
    def test_valores_basicos(self):
        self.assertEqual(Fibonacci.iteracao(0), 0)
        self.assertEqual(Fibonacci.iteracao(1), 1)
        self.assertEqual(Fibonacci.recursao_simples(0), 0)
        self.assertEqual(Fibonacci.recursao_simples(1), 1)
        self.assertEqual(Fibonacci.recursao_memoizacao(0), 0)
        self.assertEqual(Fibonacci.recursao_memoizacao(1), 1)
        self.assertEqual(Fibonacci.formula_binet(0), 0)
        self.assertEqual(Fibonacci.formula_binet(1), 1)
        self.assertEqual(Fibonacci.matriz(0), 0)
        self.assertEqual(Fibonacci.matriz(1), 1)

    def test_valores_iguais_entre_metodos(self):
        for n in range(2, 31):
            esperado = Fibonacci.iteracao(n)
            self.assertEqual(Fibonacci.recursao_simples(n), esperado)
            self.assertEqual(Fibonacci.recursao_memoizacao(n), esperado)
            self.assertEqual(Fibonacci.formula_binet(n), esperado)
            self.assertEqual(Fibonacci.matriz(n), esperado)

    def test_gerar_exemplos_respeita_termos(self):
        exemplos = {item["metodo"]: item for item in gerar_exemplos()}

        self.assertEqual(exemplos["iteracao"]["termos"], 30)
        self.assertEqual(exemplos["recursao_simples"]["termos"], 30)
        self.assertEqual(exemplos["formula_binet"]["termos"], 30)
        self.assertEqual(exemplos["recursao_memoizacao"]["termos"], 50)
        self.assertEqual(exemplos["matriz"]["termos"], 50)

        for metodo, exemplo in exemplos.items():
            self.assertIn("descricao", exemplo, metodo)
            self.assertIn("complexidade", exemplo, metodo)
            self.assertIn("tempo_ms", exemplo, metodo)
            self.assertGreaterEqual(exemplo["tempo_ms"], 0)

    def test_entrada_invalida(self):
        with self.assertRaises(ValueError):
            Fibonacci.iteracao(-1)
        with self.assertRaises(TypeError):
            Fibonacci.matriz(1.5)


if __name__ == "__main__":
    unittest.main()
