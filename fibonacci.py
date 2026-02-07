from __future__ import annotations

from time import perf_counter


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
    def recursao_simples(n: int) -> int:
        """Calcula Fibonacci com recursão simples (O(2^n))."""
        Fibonacci._validar_entrada(n)
        if n < 2:
            return n
        return Fibonacci.recursao_simples(n - 1) + Fibonacci.recursao_simples(n - 2)

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
    def formula_binet(n: int) -> int:
        """Calcula Fibonacci usando a fórmula de Binet (O(1) com precisão limitada)."""
        Fibonacci._validar_entrada(n)
        raiz_5 = 5**0.5
        phi = (1 + raiz_5) / 2
        psi = (1 - raiz_5) / 2
        return round((phi**n - psi**n) / raiz_5)

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


def gerar_exemplos() -> list[dict[str, str | int | float]]:
    """Gera exemplos com metadados e tempo de execução por método."""
    configuracoes = [
        {
            "metodo": "iteracao",
            "descricao": "Loop simples, fácil de entender e com custo linear.",
            "complexidade": "O(n)",
            "termos": 30,
        },
        {
            "metodo": "recursao_simples",
            "descricao": "Recursão direta; didática, mas bem lenta para valores altos.",
            "complexidade": "O(2^n)",
            "termos": 30,
        },
        {
            "metodo": "formula_binet",
            "descricao": "Usa fórmula matemática fechada; excelente para demonstração.",
            "complexidade": "O(1)",
            "termos": 30,
        },
        {
            "metodo": "recursao_memoizacao",
            "descricao": "Recursão com cache, reaproveita resultados e acelera bastante.",
            "complexidade": "O(n)",
            "termos": 50,
        },
        {
            "metodo": "matriz",
            "descricao": "Exponenciação de matriz, ótima performance para n grande.",
            "complexidade": "O(log n)",
            "termos": 50,
        },
    ]

    exemplos = []
    for config in configuracoes:
        metodo = getattr(Fibonacci, config["metodo"])
        inicio = perf_counter()
        valor = metodo(config["termos"])
        tempo_ms = (perf_counter() - inicio) * 1000

        exemplos.append(
            {
                "metodo": config["metodo"],
                "descricao": config["descricao"],
                "complexidade": config["complexidade"],
                "termos": config["termos"],
                "resultado": valor,
                "tempo_ms": round(tempo_ms, 4),
            }
        )

    return exemplos


def imprimir_exemplos() -> None:
    """Mostra no terminal os exemplos e informações de cada método."""
    print("Exemplos de Fibonacci por método:\n")
    for exemplo in gerar_exemplos():
        print(f"Método: {exemplo['metodo']}")
        print(f"Descrição: {exemplo['descricao']}")
        print(f"Complexidade: {exemplo['complexidade']}")
        print(f"Termos usados (n): {exemplo['termos']}")
        print(f"Resultado F(n): {exemplo['resultado']}")
        print(f"Tempo aproximado: {exemplo['tempo_ms']} ms")
        print("-" * 50)


if __name__ == "__main__":
    imprimir_exemplos()
