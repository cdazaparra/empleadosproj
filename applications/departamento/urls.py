from django.contrib import admin
from django.urls import path
from . import views

app_name = "departamento_app"

urlpatterns = [
    path('new-departamento/',views.NewDepartamentoView.as_view(), name='nuevo_departamento'),
    path('listar_departamento/',views.ListDepartamentoView.as_view(), name='departamentos'),
]
