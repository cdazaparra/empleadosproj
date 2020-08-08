from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .forms import NewDepartamentoForm
from applications.personas.models import Empleado
from applications.departamento.models import Departamento
# Create your views here.

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    def form_valid(self, form):
        print('*******************   Estamos en el form valid')
        departament = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )
        departament.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            firts_name=nombre,
            last_name=apellido,
            job='1',
            departamento=departament,            
        )
        return super(NewDepartamentoView, self).form_valid(form)

class ListDepartamentoView(ListView):
    template_name = 'departamento/list_all.html'
    model = Departamento
    context_object_name = 'departamentos'