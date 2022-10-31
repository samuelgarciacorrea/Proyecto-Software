from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


    

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
    def name(self):
        return self.first_name

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
    
    @property
    def name(self):
        return self.first_name

    @property
    def apellido(self):
        return self.last_name

    @property
    def correo(self):
        return self.email
    