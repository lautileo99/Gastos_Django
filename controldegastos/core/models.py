from django.db import models

# Create your models here.
class Registro(models.Model):
    id_gasto = models.SmallIntegerField()
    descripcion = models.TextField()
    categoria = models.TextField()
    mes = models.CharField()
    costo = models.IntegerField()