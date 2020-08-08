from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Empleado
        fields = (
            'firts_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
            'avatar',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple(),
        }