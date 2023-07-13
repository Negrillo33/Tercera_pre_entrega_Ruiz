from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from .forms import MarcaForm, ModeloForm, ClienteForm

def my_view(request):
    return HttpResponse("Lo sentimos! La pagina web a la que intenta ingresar esta en mantenimiento en estos momentos")
# pongo el return con un cartel en mantenimiento porque no logro hacer que el menu funcione y prefiero eso a que no se visualice nada 

class BuscarView(View):
    def get(self, request):
        return render(request, 'buscar.html')



class MenuView(View):
    def get(self, request):
        return render(request, 'menu.html')

class InsercionView(View):
    def get(self, request):
        marca_form = MarcaForm()
        modelo_form = ModeloForm()
        cliente_form = ClienteForm()
        return render(request, 'insercion.html', {'marca_form': marca_form, 'modelo_form': modelo_form, 'cliente_form': cliente_form})

    def post(self, request):
        marca_form = MarcaForm(request.POST)
        modelo_form = ModeloForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if marca_form.is_valid() and modelo_form.is_valid() and cliente_form.is_valid():
            marca_form.save()
            modelo_form.save()
            cliente_form.save()
            return render(request, 'exito.html')
        return render(request, 'insercion.html', {'marca_form': marca_form, 'modelo_form': modelo_form, 'cliente_form': cliente_form})



  
