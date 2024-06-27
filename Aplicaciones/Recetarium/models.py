from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=50)

# MODELO RECETAS
class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=50)
    categoria = models.CharField(max_length=255)
    temporada = models.CharField(max_length=255)
    origen = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=255)
    instrucciones = models.CharField(max_length=255)
    tiempo_preparacion = models.CharField(max_length=10)
    dificultad = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="recetas/")
    fecha_registro_receta = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "tbl_recetas"

#FIN MODELO RECETAS

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    cantidad = models.IntegerField()
    variedad = models.CharField(max_length=255, null=True, blank=True)
    usos = models.CharField(max_length=255, null=True, blank=True)
    p_nutricional = models.CharField(max_length=255, null=True, blank=True)
    consejos = models.CharField(max_length=255, null=True, blank=True)
    grasas_saturadas = models.IntegerField(null=True, blank=True)
    calorias = models.IntegerField(null=True, blank=True)
    hidratos_de_carbono = models.IntegerField(null=True, blank=True)
    grasas_trans = models.IntegerField(null=True, blank=True)
    total_carbohidratos = models.IntegerField(null=True, blank=True)
    azucares = models.IntegerField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)  # Relación con Receta

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "tbl_ingredientes"


# MODELO CONSEJEROS
class Consejero(models.Model):
    id_consejero = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="consejeros/")
    nombre = models.CharField(max_length=225)
    apellido = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=255)
    edad = models.IntegerField()
    idioma = models.CharField(max_length=225)
    fecha_nacimiento = models.DateField()
    titulacion = models.CharField(max_length=225)
    pais = models.TextField()
    experiencia = models.CharField(max_length=225)
    descripcion = models.CharField(max_length=225)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_consejeros"


#FIN MODELO CONSEJEROS

#MODELO ROLES

class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    permisos = models.CharField(max_length=255)

    class Meta:
        db_table = "tbl_roles"

#FIN MODELO ROLES

#MODELO DIETAS

class Dieta(models.Model):
    id_dieta_c = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to="dietas/")
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
    fecha_registro_dieta = models.DateTimeField(auto_now_add=True)
    consejero = models.ForeignKey(Consejero, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # Campos de comidas opcionales
    dia_semana = models.CharField(max_length=20, null=True, blank=True)
    desayuno = models.CharField(max_length=255, null=True, blank=True)
    media_manana = models.CharField(max_length=255, null=True, blank=True)
    almuerzo = models.CharField(max_length=255, null=True, blank=True)
    merienda = models.CharField(max_length=255, null=True, blank=True)
    cena = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "tbl_dieta_calendario"

#FIN MODELOS DIETAS

#MODELO INGREDIENTES

class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    cantidad = models.IntegerField()
    variedad = models.CharField(max_length=255, null=True, blank=True)
    usos = models.CharField(max_length=255, null=True, blank=True)
    p_nutricional = models.CharField(max_length=255, null=True, blank=True)
    consejos = models.CharField(max_length=255, null=True, blank=True)
    grasas_saturadas = models.IntegerField(null=True, blank=True)
    calorias = models.IntegerField(null=True, blank=True)
    hidratos_de_carbono = models.IntegerField(null=True, blank=True)
    grasas_trans = models.IntegerField(null=True, blank=True)
    total_carbohidratos = models.IntegerField(null=True, blank=True)
    azucares = models.IntegerField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    fecha_registro_ingredientes = models.DateTimeField(auto_now_add=True)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "tbl_ingredientes"
