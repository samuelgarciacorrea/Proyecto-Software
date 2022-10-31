from pyexpat.errors import messages
import re
from django.shortcuts import render, redirect
from .models import  Usuario
from django.contrib.auth import authenticate, login as userlogin, logout as userlogout, get_user_model

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def about(request):
    usuarios = Usuario.objects.all()
    data = {
        'nombre': usuarios,
    } 
    return render(request, 'about.html',data)


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def Department(request):
    return render(request, 'Department.html', {})

def historias(request):
    return render(request, 'history.html', {})


def Doctors(request):
    return render(request, 'Doctors.html', {})


def elements(request):
    return render(request, 'elements.html', {})


def main(request):
    return render(request, 'main.html', {})

def citas(request):
    return render(request, 'citas.html', {})

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


