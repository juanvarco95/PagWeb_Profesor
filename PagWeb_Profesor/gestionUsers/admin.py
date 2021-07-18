from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email')
    search_fields = ('name', 'last_name', 'email')


admin.site.register(Usuario, UsuarioAdmin)



