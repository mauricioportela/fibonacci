class Fibonacci:
    """Implementações de Fibonacci com diferentes estratégias."""

    @staticmethod
    def iteracao(n: int) -> int:
        """Calcula Fibonacci usando iteração (O(n))."""
        Fibonacci._validar_entrada(n)
        if n < 2:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def recursao_memoizacao(n: int) -> int:
        """Calcula Fibonacci via recursão com memoização (O(n))."""
        Fibonacci._validar_entrada(n)
        memo = {0: 0, 1: 1}

        def fib(k: int) -> int:
            if k not in memo:
                memo[k] = fib(k - 1) + fib(k - 2)
            return memo[k]

        return fib(n)

    @staticmethod
    def matriz(n: int) -> int:
        """Calcula Fibonacci com exponenciação de matriz (O(log n))."""
        Fibonacci._validar_entrada(n)
        if n == 0:
            return 0

        base = ((1, 1), (1, 0))
        resultado = Fibonacci._potencia_matriz(base, n - 1)
        return resultado[0][0]

    @staticmethod
    def _potencia_matriz(matriz: tuple[tuple[int, int], tuple[int, int]], expoente: int) -> tuple[tuple[int, int], tuple[int, int]]:
        resultado = ((1, 0), (0, 1))  # identidade
        base = matriz

        while expoente > 0:
            if expoente % 2 == 1:
                resultado = Fibonacci._multiplicar_matriz(resultado, base)
            base = Fibonacci._multiplicar_matriz(base, base)
            expoente //= 2

        return resultado

    @staticmethod
    def _multiplicar_matriz(a: tuple[tuple[int, int], tuple[int, int]], b: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
        return (
            (
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ),
            (
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ),
        )

    @staticmethod
    def _validar_entrada(n: int) -> None:
        if not isinstance(n, int):
            raise TypeError("n deve ser um inteiro")
        if n < 0:
            raise ValueError("n deve ser maior ou igual a zero")
