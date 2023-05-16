from django.db import models

# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)


# Hace falta ponerlo para que en el panel de administrador se muestre con el nombre y no como [object object]
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)

    apellido = models.CharField(max_length=50)

    nacimiento = models.DateField(null=True)

    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)

# Hace falta ponerlo para que en el panel de administrador se muestre con el nombre y no como [object object]
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
