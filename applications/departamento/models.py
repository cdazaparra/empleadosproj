from django.db import models

class Departamento(models.Model):
    name = models.CharField("Nombre", max_length=50, null=True, unique=True)
    shor_name = models.CharField("shor_name", max_length=20, blank=True, null=True, unique=True)
    estado = models.BooleanField("Estado", default=False)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Mis Departamentos'
#        ordering = ['-name']
#        unique_together = ('name','shor_name')
        
        
    def __str__(self):
        return str(self.id)+'-'+self.name +'-'+self.shor_name
    