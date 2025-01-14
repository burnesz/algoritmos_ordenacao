from django.shortcuts import render
from app.forms import FormArray
from .utils import main

def home(request):
    if request.method == "GET":
        form = FormArray()
        context = {'form': form}
    elif request.method == "POST":
        form = FormArray(request.POST)
        context = {'form': form}
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            tamanho = form.cleaned_data['tamanho']
            algoritmo = form.cleaned_data['algoritmo']
            params = (tipo, tamanho, algoritmo)
            main.main(params)
    return render(request, "index.html", context=context)