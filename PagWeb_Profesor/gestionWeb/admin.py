from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento')
    search_fields = ('nombre', 'apellido','documento')

admin.site.register(Usuario, UsuarioAdmin)

