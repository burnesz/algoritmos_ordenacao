from algoritmos.algoritmo import Algoritmo
import random

class QuickSort(Algoritmo):
    def sort(self, A):
        self._quick_sort(A, 0, len(A) - 1)
        self.grafico_array(A)

    def _quick_sort(self, A, inicio, fim):
        self.grafico_array(A)
        if inicio < fim:
            p = random.randint(inicio,fim)
            A[p], A[fim] = A[fim], A[p]
            
            x = self.particiona(A, inicio, fim)
            self._quick_sort(A, inicio, x-1)
            self._quick_sort(A, x+1, fim)

    def particiona(self, A, inicio, fim):
        pivo = A[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            if A[j] <= pivo:
                i += 1
                A[i], A[j] = A[j], A[i]
                
        A[i+1], A[fim] = A[fim], A[i+1]
        return i+1
