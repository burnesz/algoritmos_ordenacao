from algoritmos.algoritmo import Algoritmo

class HeapSort(Algoritmo):
    def sort(self, A):
        self._heap_sort(A)
        self.grafico_array(A)

    def corrige_heap_descendo(self, H, i, n):
        self.grafico_array(H)
        maior = i
        filho_esq = 2 * i + 1
        filho_dir = 2 * i + 2

        if filho_esq < n:
            if H[filho_esq] > H[maior]:
                maior = filho_esq

        if filho_dir < n:
            if H[filho_dir] > H[maior]:
                maior = filho_dir

        if maior != i:
            H[i], H[maior] = H[maior], H[i]
            self.corrige_heap_descendo(H, maior, n)

    def constroi_heap(self, H):
        n = len(H)

        for i in range(n // 2 - 1, -1, -1):
            self.corrige_heap_descendo(H, i, n)

    def _heap_sort(self, A):
        n = len(A)
        self.constroi_heap(A)

        for i in range(n - 1, 0, -1):
            A[0], A[i] = A[i], A[0]
            self.corrige_heap_descendo(A, 0, i)