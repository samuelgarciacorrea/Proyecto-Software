from pyexpat.errors import messages
import re
from .forms import formularioContacto, AgendarCita, Historia
from django.shortcuts import render, redirect
from .models import  Usuario, Doctores,Historia,Cita
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout, get_user_model

# Create your views here.


def index(request):
    return render(request, 'index.html')

def citas(request):
    citas = Cita.objects.all()
    data = {
        'lista_citas': citas,
    } 
    return render(request, 'citas.html',data)

def historiaClinica(request):
    historias = Historia.objects.all()
    data = {
        'lista_historias': historias,
    } 
    return render(request, 'historias.html',data)


def about(request):
    usuarios = Usuario.objects.all()
    data = {
        'nombre': usuarios,
    } 
    return render(request, 'about.html',data)


def blog(request):
    return render(request, 'blog.html', )

def denegado(request):
    return render(request, 'denegado.html', )

def agendarCita(request):
    data = {
        'form': AgendarCita()
    }
    if request.method == 'POST':
        formulario = AgendarCita(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reseña enviada"
        else:
            data["form"] = formulario
    return render(request, 'agendarCita.html',data )


def contact(request):
    data = {
        'form': formularioContacto()
    }
    if request.method == 'POST':
        formulario = formularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reseña enviada"
        else:
            data["form"] = formulario
    return render(request, 'contact.html',data )


def Department(request):
    return render(request, 'Department.html', )

def historias(request):
    data = {
        'form': Historia()
    }
    if request.method == 'POST':
        formulario = Historia(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Reseña enviada"
        else:
            data["form"] = formulario
    
    return render(request, 'history.html',data)


def Doctors(request):
    doctores = Doctores.objects.all()
    cant_doctores = len(doctores)
    data = {
        'lista_doctores': doctores,
        'items': cant_doctores
    }
    return render(request, 'Doctors.html',data )

def Doctor(request, name_p):
    doctor = Doctores.objects.get(name=name_p)
    data = {
        'doctor': doctor,
    }
    return render(request, "Doctores.html", data)


def elements(request):
    return render(request, 'elements.html', {})


def main(request):
    return render(request, 'main.html', {})


def login(request):

    if request.user.is_authenticated:
        return redirect("index")

    error = False
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")

    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userlogin(request, user)
            return redirect("index")
        else:
            error = True

    return render(request, "login.html", {
        "error": error
    })

def logout(request):
    userlogout(request)
    return redirect("login")

def registro(request):
    error=False
    nombre_campos = [
        "nombre",
        "apellidos",
        "cedula",
        "correo",
        "celular",
        "clave",
        "direccion",
        "fecha",
        "sexo",
        "rh",
        "eps",
        "enfermedades",
        "medicamentos",
        "alergias",
        
    ]

    campos = {
        nombre: request.POST.get(nombre, "")
        for nombre in nombre_campos
    }

    crear_usuario = campos.get("nombre")
    if crear_usuario:
        campos.update({
            "first_name":campos.get("nombre"),
            "last_name":campos.get("apellidos"),
            "username":campos.get("nombre"),
            "email":campos.get("correo"),
            "password":campos.get("clave"),
            "fecha_nacimiento":campos.get("fecha")
        })

        borrar_campos = ("nombre","apellidos","correo","clave","fecha")

        for campo in borrar_campos:
            campos.pop(campo, None)

        user = Usuario.objects.create_user(**campos)

        if user is not None:
            userlogin(request, user)
            return redirect("index")
        else:
            error = True

    return render(request, "register.html", {"error":error})


