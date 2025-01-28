import io
import matplotlib.pyplot as plt

class Algoritmo:
    def __init__(self):
        self.contador = 0
        self.graficos = []

    def grafico_array(self, A):
        # Criar o gráfico
        plt.figure(figsize=(19.2, 10.8))
        plt.bar(range(len(A)), A, color="blue")
        plt.title(f"Array {self.contador}")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.grid()
        plt.tight_layout()

        buffer = io.BytesIO()
        plt.savefig(buffer, format='jpg')
        buffer.seek(0) 
        self.graficos.append(buffer)  
        plt.close()

        self.contador += 1
