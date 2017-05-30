from django import forms

from .models import Asistencia


class AsistenciaForm(forms.Form):
    nombres = forms.CharField(label="nombre(s) del alumno")
    apellidos = forms.CharField(label="apellidos del alumno")
    clase = forms.CharField(label="clase del alumno")
    hora = forms.CharField(label="hora de clase")
    presente = forms.BooleanField()





    # def clean(self):
    #
    #     data = self.cleaned_data
    #
    #     return data
