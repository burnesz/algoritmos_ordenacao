from .gera_array import GeraArray
from .algoritmos.quick_sort import QuickSort
from .algoritmos.heap_sort import HeapSort
from .algoritmos.merge_sort import MergeSort
import os
import cv2
import numpy as np
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
        video = cv2.VideoWriter("./app/static/videos/ordenacao.mp4", fourcc, 10, (largura, altura))

        # Adicionar as imagens ao vídeo
        for buffer in graficos:
            image = Image.open(buffer)
            imagem_np = np.array(image)  # Converte a imagem para o formato NumPy
            imagem_bgr = cv2.cvtColor(imagem_np, cv2.COLOR_RGB2BGR)  # OpenCV usa BGR em vez de RGB
            video.write(imagem_bgr)

        video.release()
        convert_video()

def main(params):
    gera_array = GeraArray()
    tipos_array = ["aleatorio", "quase_ordenado", "ordenado_descr"]
    algoritmos = [QuickSort(), HeapSort(), MergeSort()]

    tipo_array, tamanho_array, algoritmo = params

    algoritmo_obj = algoritmos[algoritmo]
    metodo_array = getattr(gera_array, tipos_array[tipo_array])

    A = metodo_array(tamanho_array)
    print(A)
    algoritmo_obj.sort(A)
    print(A)
    
    gera_video(algoritmo_obj.graficos)

def convert_video():
    os.system("ffmpeg -i ./app/static/videos/ordenacao.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -movflags +faststart ./app/static/videos/ordenacao_h264.mp4")
