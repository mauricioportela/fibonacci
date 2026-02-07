import unittest

from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    def test_valores_basicos(self):
        self.assertEqual(Fibonacci.iteracao(0), 0)
        self.assertEqual(Fibonacci.iteracao(1), 1)
        self.assertEqual(Fibonacci.recursao_memoizacao(0), 0)
        self.assertEqual(Fibonacci.recursao_memoizacao(1), 1)
        self.assertEqual(Fibonacci.matriz(0), 0)
        self.assertEqual(Fibonacci.matriz(1), 1)

    def test_valores_iguais_entre_metodos(self):
        for n in range(2, 31):
            esperado = Fibonacci.iteracao(n)
            self.assertEqual(Fibonacci.recursao_memoizacao(n), esperado)
            self.assertEqual(Fibonacci.matriz(n), esperado)

    def test_entrada_invalida(self):
        with self.assertRaises(ValueError):
            Fibonacci.iteracao(-1)
        with self.assertRaises(TypeError):
            Fibonacci.matriz(1.5)


if __name__ == "__main__":
    unittest.main()
