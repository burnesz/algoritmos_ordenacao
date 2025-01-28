import os
from django.shortcuts import render
from app.forms import FormArray
from .utils import main

path_video = './app/static/videos/ordenacao_h264.mp4'

print(path_video.replace('_h264', ''))

def home(request):
    if request.method == "GET":
        if check_video(path_video):
            os.system(f"rm {path_video} {path_video.replace('_h264', '')}")
        form = FormArray()
        context = {'form': form,}
    
        return render(request, "index.html", context=context)

    elif request.method == "POST":
        form = FormArray(request.POST)
        
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            tamanho = form.cleaned_data['tamanho']
            algoritmo = form.cleaned_data['algoritmo']
            params = (tipo, tamanho, algoritmo)
            main.main(params)
            while True:
                if check_video(path_video):
                    print('Video criado')
                    break
            return video(request)

def video(request):
    return render(request, "video.html")

def check_video(path):
    if os.path.exists(path):
        return True
    else:
        return False
