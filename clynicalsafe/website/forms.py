from django import forms
from .models import Contacto, Cita

class formularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["mensaje","nombre","correo","tema"]
        
        
class AgendarCita(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ["fecha1","fecha2","Departamento","Doctor","nombre","celular","correo"]
        
