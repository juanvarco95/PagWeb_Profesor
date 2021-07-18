from django.db import models


class Usuario(models.Model):
    username = models.CharField('UserName',max_length = 255, unique = True, null = True)
    name = models.CharField('Name',max_length = 255)
    last_name = models.CharField('Last Name',max_length = 255, null = True)
    image = models.ImageField('Image',upload_to = 'perfil/', null = True)
    email = models.EmailField('Email', max_length = 255, unique = True, null = True)
    cellPhone = models.CharField('Cellphone' ,max_length = 30)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def natural_key(self):
        return self.name



    def __str__(self):
        return f'{self.name} {self.last_name}'
