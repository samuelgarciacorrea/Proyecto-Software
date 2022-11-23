from django.contrib import admin
from .models import Usuario, Doctores, Contacto, Cita
# Register your models here.


admin.site.register(Usuario)
admin.site.register(Doctores)
admin.site.register(Contacto)
admin.site.register(Cita)
