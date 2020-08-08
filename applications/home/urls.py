from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PruebaList.as_view()),
    path('foundation/',views.PruebaFoundationView.as_view()),
    path('inserta/',views.PruebaCreateView.as_view(), name='prueba_add'),
]