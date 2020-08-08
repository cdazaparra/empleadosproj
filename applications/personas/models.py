from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=60)    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
#        orderin = ['last_name']        
    def __str__(self):
        return str(self.id)+'-'+self.habilidad

class Empleado(models.Model):
    JOB_CHOICES =(
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Desarrollador'),
        ('3','Analista'),
    )
    firts_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombre Completo',max_length=200, blank=True, null=True)
    job = models.CharField('Trabajo',max_length=50, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
#        orderin = ['last_name']
        
    def __str__(self):
        return str(self.id)+'-'+self.firts_name +'-'+self.last_name
