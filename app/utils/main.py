from gera_array import GeraArray
from algoritmos.quick_sort import QuickSort
from algoritmos.heap_sort import HeapSort
from algoritmos.merge_sort import MergeSort
import cv2
import re
import os
import numpy as np
import io
from PIL import Image

def gera_video(graficos):
        # Usando os gráficos armazenados em memória para criar o vídeo
        if not graficos:
            print("Nenhuma imagem disponível para gerar o vídeo.")
            return

        # Carregar o primeiro gráfico para pegar as dimensões
        buffer_inicial = graficos[0]
        image = Image.open(buffer_inicial)
        imagem_np = np.array(image)
        altura, largura, canais = imagem_np.shape

        # Inicializar o VideoWriter
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para .mp4
        video = cv2.VideoWriter("./resultado/ordenacao.mp4", fourcc, 10, (largura, altura))

        # Adicionar as imagens ao vídeo
        for buffer in graficos:
            image = Image.open(buffer)
            imagem_np = np.array(image)  # Converte a imagem para o formato NumPy
            imagem_bgr = cv2.cvtColor(imagem_np, cv2.COLOR_RGB2BGR)  # OpenCV usa BGR em vez de RGB
            video.write(imagem_bgr)

        video.release()

def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')

def menu():
    clear_terminal()
    tipo_array = int(input('''
        Escolha qual tipo de array você deseja ordenar:

        1 - Valores aleatórios.

        2 - Valores quase ordenados.

        3 - Valores Ordenados Descrescentemente.
        '''))
    tamanho_array = int(input('''
        Escolha qual tamanho de array você deseja ordenar:
        '''))
    algoritmo = int(input('''
        Escolha qual algoritmo você deseja usar para ordenar o array:

        1 - Quick Sort.

        2 - Heap Sort.

        3 - Merge Sort.            
        
        '''))
    return tipo_array-1, tamanho_array, algoritmo-1

def main():
    gera_array = GeraArray()
    tipos_array = ["aleatorio", "quase_ordenado", "ordenado_descr"]
    algoritmos = [QuickSort(), HeapSort(), MergeSort()]

    tipo_array, tamanho_array, algoritmo = menu()

    algoritmo_obj = algoritmos[algoritmo]
    metodo_array = getattr(gera_array, tipos_array[tipo_array])

    A = metodo_array(tamanho_array)   
    algoritmo_obj.sort(A)
    print(A)
    
    gera_video(algoritmo_obj.graficos)

if __name__ == "__main__":
    main()
