from django import forms
from .models import Contacto, Cita, Historia

class formularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["mensaje","nombre","correo","tema"]
        
        
class AgendarCita(forms.ModelForm):

    class Meta:
        model = Cita
        fields = ["fecha1","fecha2","Departamento","Doctor","nombre","celular","correo"]
        
  
class Historia(forms.ModelForm):

    class Meta:
        model = Historia
        fields = ["fecha","Doctor","nombre","apellido1","apellido2","sexo","Ocupacion","edad","estadoCivil","correo","direccion","ciudad","pais","celular","Observaciones","rh","eps","enfermedades","medicamentos","alergias","alergiasMedicamentos"]
        

