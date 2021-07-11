from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    documento = models.IntegerField(null = True)
    correo = models.EmailField(max_length = 50)
    celular = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre