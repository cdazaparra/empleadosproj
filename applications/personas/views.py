from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from .forms import EmpleadoForm

class ListAllEmpleados(ListView):
    template_name = 'personas/list_all.html'
    model = Empleado

class ListAllEmpleadosPaginados(ListView):
    template_name = 'personas/list_paginados.html'
    paginate_by = 4
    #model = Empleado
    def get_queryset(self):
        palabra = self.request.GET.get("palabraClave",'')
        queryset = Empleado.objects.filter(
            firts_name__icontains=palabra
        )
        return queryset

class ListAllEmpleadosAdmin(ListView):
    template_name = 'personas/list_empleados.html'
    paginate_by = 6
    def get_queryset(self):
        palabra = self.request.GET.get("palabraClave",'')
        queryset = Empleado.objects.filter(
            firts_name__icontains=palabra
        )
        return queryset

class ListAllEmpleadosArea(ListView):
    template_name = 'personas/list_all_area.html'
    queryset = Empleado.objects.filter(
        departamento__name = 'Personal'
    )

class ListAllEmpleadosArea2(ListView):
    template_name = 'personas/list_all_area2.html'    
    def get_queryset(self):
        area = self.kwargs['shorname']
        queryset = Empleado.objects.filter(
            departamento__shor_name = area
        )
        return queryset

class ListAllEmpleadosPalabra(ListView):
    template_name = 'personas/list_all_palabra.html'
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra = self.request.GET.get("palabraClave",'')
        queryset = Empleado.objects.filter(
            firts_name = palabra
        )
        return queryset

class ListAllHabilidades(ListView):
    template_name = 'personas/list_habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        identificador = self.request.GET.get("identificado",'') 
        empleado = Empleado.objects.get(id=identificador)
        print(empleado.firts_name)
        #queryset = Empleado.objects.filter(
        #    id = identificador
        #)
        return empleado.habilidades.all

class EmpleadoDetail(DetailView):
    model = Empleado
    template_name='personas/detail_empleado.html'


class SuccessView(TemplateView):
    template_name = "personas/success.html"


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "personas/update.html"
    fields = ['firts_name','last_name','job','departamento','habilidades',]
    success_url = reverse_lazy('persona_app:empleados_admin')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "personas/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

class InicioView(TemplateView):
    template_name = 'inicio.html'

class EmpleadoCreateView(CreateView):
    template_name = "personas/crear_empleado.html"
    model = Empleado
    #fields = ('__all__')
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.firts_name+' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
