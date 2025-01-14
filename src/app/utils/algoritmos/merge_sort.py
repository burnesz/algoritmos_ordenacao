from .algoritmo import Algoritmo

class MergeSort(Algoritmo):
    def sort(self, A):
        self._merge_sort(A, 0, len(A) - 1)
        self.grafico_array(A)

    def combina(self, A, inicio, meio, fim):
        n_um = meio - inicio + 1
        n_dois = fim - meio

        B = [0] * n_um
        C = [0] * n_dois
        
        for i in range(n_um):
            B[i] = A[inicio + i]
            
        for j in range(n_dois):
            C[j] = A[meio + j + 1]
             
        i = 0
        j = 0
        k = inicio
        
        while i < n_um and j < n_dois:
            if B[i] < C[j]:
                A[k] = B[i]
                i += 1
            else:
                A[k] = C[j]
                j += 1

            k += 1
            
        while i < n_um:
            A[k] = B[i]
            i += 1
            k += 1
            
        while j < n_dois:
            A[k] = C[j]
            j += 1
            k += 1
            
    def _merge_sort(self, A, inicio, fim):
        self.grafico_array(A)
        if inicio < fim:
            meio = (inicio + fim) // 2
            self._merge_sort(A, inicio, meio)
            self._merge_sort(A, meio + 1, fim)
            self.combina(A, inicio, meio, fim)
