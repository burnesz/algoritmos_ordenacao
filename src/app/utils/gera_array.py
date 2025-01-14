import random

class GeraArray:
    def __init__(self):
        pass

    def ordenado_descr(self, n):
        A = [i for i in range(n-1, -1, -1)]
        return A

    def quase_ordenado(self, n):
        A = [i for i in range(n)]

        for _ in range(n // 10):  
            i, j = random.sample(range(n), 2)  
            A[i], A[j] = A[j], A[i]

        return A

    def aleatorio(self, n):
        A = random.sample(range(n), n)
        return A