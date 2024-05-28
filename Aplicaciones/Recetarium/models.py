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

class Consejero(models.Model):
    id_consejero = models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=255)
    nombre = models.CharField(max_length=225)
    apellido = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=225)
    edad = models.IntegerField()
    idioma = models.CharField(max_length=225)
    fecha_nacimiento = models.DateField()
    titulacion = models.CharField(max_length=225)
    pais = models.TextField()
    experiencia = models.CharField(max_length=225)

    class Meta:
        db_table = 'tbl_consejeros'

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_roles'
