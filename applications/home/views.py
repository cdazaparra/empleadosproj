from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# Se importan los modelos
from .models import Prueba
# Create your views here.
from .forms import PruebaForm
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


# Se crea el modelo Prueba en models.py (1)
# Se importan los modelos from .models import Prueba (2)
# Se crea la clase PruebaList (3)
# Se crea el template home/lista.html (4) 
# Se crea el path('lista/',views.PruebaList.as_view()), en urls.py del home (5)
# Se importa CreateView (6), esto es para crea registros createview
# Se crea la clase PruebaCreateView (7)
# Se crea el template home/inserta.html (8) si se usa {{ form }} carga auomaticamente el formulario
# Se crea el path('inserta/',views.PruebaCreateView.as_view()), en urls.py del home (9)
# Se actualiza success_url = '/' (10)
# Se crea el archivo forms.py
# Se importa en views.py el forms.py
# Se cambia el fields por form_class

# Vista para listar objetos
class PruebaList(ListView):
    template_name= 'home/lista.html'
    model = Prueba
    context_object_name = 'lista'

# Vista para listar objetos
class PruebaFoundationView(TemplateView):
    template_name= 'home/pruebafoundation.html'
    model = Prueba
    context_object_name = 'lista'

# Vista para insertar objetos
class PruebaCreateView(CreateView):
    template_name = "home/inserta.html"
    model = Prueba
    # Se indica lo que se va aregistrar en el modelo
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    success_url = '/'


