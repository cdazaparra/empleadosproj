from django.contrib import admin
from django.urls import path
from . import views
app_name = "persona_app"

urlpatterns = [
    path('listar-todo/',views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-paginado/',views.ListAllEmpleadosPaginados.as_view(), name='empleados_all_pag'),
    path('listar-todo-area/',views.ListAllEmpleadosArea.as_view()),
    path('listar-todo-area2/<shorname>',views.ListAllEmpleadosArea2.as_view(), name='empleados_area'),
    path('buscar-empleado/',views.ListAllEmpleadosPalabra.as_view()),
    path('habilidades/',views.ListAllHabilidades.as_view()),
    path('empleados_admin/',views.ListAllEmpleadosAdmin.as_view(),name='empleados_admin'),
    path('detalles/<pk>',views.EmpleadoDetail.as_view(), name='empleado_detalle'),
    path('',views.InicioView.as_view(),name='inicio'),
    path('guardado/',views.SuccessView.as_view(), name='correcto'),
    path('crear/',views.EmpleadoCreateView.as_view(), name='add'),
    path('actualizar/<pk>/',views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('borrar/<pk>/',views.EmpleadoDeleteView.as_view(), name='borrar_empleado'),
]