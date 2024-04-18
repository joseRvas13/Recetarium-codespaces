from django.db import models

class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=50)
    imagen = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=255)
    tiempo_preparacion = models.CharField(max_length=10)
    dificultad = models.CharField(max_length=20)

    class Meta:
        db_table = 'tbl_recetas'