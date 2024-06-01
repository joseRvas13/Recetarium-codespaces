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


class Dieta(models.Model):
    id_dieta_c = models.AutoField(primary_key=True)
    imagen = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=255)
    calorias = models.IntegerField()
    condicion_medica = models.CharField(max_length=255)
    valor_nutricional = models.IntegerField()
    actividad_fisica = models.CharField(max_length=255)
    consejos = models.CharField(max_length=255)
    dispositivos = models.CharField(max_length=255)
    bibliografia = models.CharField(max_length=255)
    consejero_id = models.IntegerField(null=True, blank=True)
    dia_semana = models.CharField(max_length=20, null=True, blank=True)
    desayuno = models.CharField(max_length=255, null=True, blank=True)
    media_manana = models.CharField(max_length=255, null=True, blank=True)
    almuerzo = models.CharField(max_length=255, null=True, blank=True)
    merienda = models.CharField(max_length=255, null=True, blank=True)
    cena = models.CharField(max_length=255, null=True, blank=True)
    usuario_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tbl_dieta_calendario'