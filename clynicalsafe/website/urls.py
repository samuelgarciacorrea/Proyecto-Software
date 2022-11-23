from django.urls import path
from . import views


urlpatterns = [
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("agendarCita.html", views.agendarCita, name="cita"),
    path("Department.html", views.Department, name="Department"),
    path("Doctors.html", views.Doctors, name="Doctors"),
    path("main.html", views.main, name="main"),
    path("register.html", views.registro, name="register"),
    path("login.html", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("citas.html/", views.citas, name="citas"),
    path("historias.html/", views.historiaClinica, name="historiaClinica"), 
    path("Doctor/denegado.html", views.denegado, name="denegado"),
    path("history.html/", views.historias, name="historias"),
    path("Doctor/<name_p>", views.Doctor),
    
]
