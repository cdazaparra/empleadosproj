from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        'firts_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    search_fields = ('firts_name',)
    list_filter = ('job','habilidades','departamento','id',)
    filter_horizontal = ('habilidades',)
    
    def full_name(self, obj):
        return obj.firts_name+' '+obj.last_name

admin.site.register(Empleado, EmpleadoAdmin)