from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tema = models.CharField(max_length=50)
    mensaje = models.TextField()
    def _str_(self):
        return self.nombre
    
Departamentos1 = [
    [0, "oftalmologia"],
    [1, "Dermatologia"],
    [2, "Patologia"],
    [3, "Consulta"],
    [4, "Operaciones"],
    [5, "Odontologia"],
]
class Cita(models.Model):
    fecha1 = models.DateField()
    fecha2 = models.DateField()
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    Departamento =  models.IntegerField(choices=Departamentos1)
    celular = models.CharField(max_length=40, null=True)
    Doctor = models.CharField(max_length=50)
    def _str_(self):
        return self.nombre
    
class Historia(models.Model):
    fecha = models.DateField()
    Doctor = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    Ocupacion = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    estadoCivil = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=128)
    pais = models.CharField(max_length=128)
    celular = models.CharField(max_length=40, null=True)
    Observaciones = models.CharField(max_length=200, null=True)
    rh = models.CharField(max_length=16,null=True)
    eps = models.CharField(max_length=16,null=True)
    enfermedades = models.CharField(max_length=1000, null=True)
    medicamentos = models.CharField(max_length=1000 , null=True)
    alergias = models.CharField(max_length=1000 , null=True)
    alergiasMedicamentos = models.CharField(max_length=1000 , null=True)

    
    

class Usuario(User):
    
    cedula = models.CharField(max_length=40, null=True)
    celular = models.CharField(max_length=40, null=True)
    direccion = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=16, null=True)
    rh = models.CharField(max_length=16,null=True)
    eps = models.CharField(max_length=16,null=True)
    enfermedades = models.CharField(max_length=1000, null=True)
    medicamentos = models.CharField(max_length=1000 , null=True)
    alergias = models.CharField(max_length=1000 , null=True)

    @property
    def nombre(self):
        return self.nombre

    @property
    def apellido(self):
        return self.last_name

    @property
    def correo(self):
        return self.email

    def __str__(self):
        return self.nombre
    
Departamentos = [
    [0, "oftalmologia"],
    [1, "Dermatologia"],
    [2, "Patologia"],
    [3, "Consulta"],
    [4, "Operaciones"],
    [5, "Odontologia"],
]    

class Doctores(User):
    cedula = models.CharField(max_length=40, null=True)
    Departamento =  models.IntegerField(choices=Departamentos)
    """ foto = models.ImageField(upload_to="doctores", null=True)
     """
    name = models.CharField(max_length=40, null=True)

    @property
    def apellido(self):
        return self.last_name

    @property
    def correo(self):
        return self.email
    