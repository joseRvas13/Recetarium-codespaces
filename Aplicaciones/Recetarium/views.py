from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Consejero, Receta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django.db.models import Q
#region INDEX
def index(request):
    return render(request, 'index.html')
#endregion 
def crear_elegir_receta(request):
    return render(request, 'Crear_Elegir_Receta.html')
 
def olvido_contraseña(request):
    return render(request, 'Olvido_Contraseña.html')

def inicio_sesion_registro(request):
    return render(request, 'Inicio_Sesion_Registro.html')

def salud_nutricion(request):
    return render(request, 'Salud_y_Nutricion.html')


def calculadora_salud(request):
    return render(request, 'Calculadora_De_Salud.html')

def signin(request):
    return render(request, 'signin.html')


#region SOPORTE TECNICO 
def soporte_tecnico(request):
    return render(request, 'soporte_tecnico.html')
#end

#region FORMULARIO DE CREAR RECETAS (USUARIO)
def receta_crear(request):
    return render(request, 'receta_crear.html')
#endregion


def invalid_page(request):
    return render(request, 'invalid_page.html')

# PÁGINA RECETAS DISPONIBLES
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def lista_consejeros(request):
    consejeros = Consejero.objects.all()
    return render(request, 'lista_consejeros.html', {'consejeros':consejeros})

#region paginacion consejeros
def lista_consejeros(request):
    consejeros_list = Consejero.objects.all().order_by('id_consejero')  # Asegúrate de que el nombre del modelo es Consejero
    consejeros_por_pagina = 9
    paginator = Paginator(consejeros_list, consejeros_por_pagina)

    page = request.GET.get('page')
    try:
        consejeros = paginator.page(page)
    except PageNotAnInteger:
        consejeros = paginator.page(1)
    except EmptyPage:
        consejeros = paginator.page(paginator.num_pages)

    return render(request, 'lista_consejeros.html', {'consejeros': consejeros})

#endregion

#region PÁGINA DETALLES DE LAS RECETAS POR SU ID
def detalle_receta(request, id_receta):
    receta = Receta.objects.get(pk=id_receta)
    return render(request, 'detalle_receta.html', {'receta': receta})
#endregion

#region PÁGINACION RECETAS DISPONIBLES
def lista_recetas(request):
    recetas_list = Receta.objects.all()
    recetas_por_pagina = 21
    paginator = Paginator(recetas_list, recetas_por_pagina)
    page_number = request.GET.get('page')
    
    # Verificar si el parámetro de página está presente
    if page_number is None:
        # Si no hay parámetro de página, redirigir a la primera página
        return render(request, 'lista_recetas.html', {'recetas': paginator.page(1)})

    try:
        recetas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la página de error personalizada
        return render(request, 'invalid_page.html')  # Redirigir a la página de error
    except EmptyPage:
        # Si el número de página está fuera del rango, mostrar la página de error personalizada
        return render(request, 'invalid_page.html')  # Redirigir a la página de error
    
    return render(request, 'lista_recetas.html', {'recetas': recetas})
#endregion


#region SIGNUP
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Verificar si el correo electrónico ya existe en la base de datos
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                # Si el correo electrónico ya existe, mostrar un mensaje de error
                return render(request, 'signup.html', {'form': form, 'error_message': 'El correo electrónico ya está en uso. Por favor, utiliza otro.'})
            else:
                # Si el correo electrónico es único, guardar el formulario y crear el usuario
                form.save()
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(email=email, password=password)
                login(request, user)
                # No establecer signup_success en la sesión aquí
                return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'index.html')

#endregion

#region FUNCIONALIAD BUSQUEDA DE RECETAS (RECETAS DISPONIBLES)
def buscar_recetas(request):
    query = request.GET.get('search')
    categoria = request.GET.get('categoria')
    dificultad = request.GET.get('dificultad')
    tiempo_preparacion = request.GET.get('tiempo_preparacion')
    
    # Eliminar caracteres no alfabéticos de la consulta
    query = re.sub(r'[^a-zA-Z\s]', '', query) if query else None
    
    # Construir la consulta principal para la búsqueda de recetas
    consulta = Q()
    if query:
        consulta &= Q(nombre_plato__icontains=query)
    if categoria:
        consulta &= Q(categoria=categoria)
    if dificultad:
        consulta &= Q(dificultad=dificultad)
    if tiempo_preparacion:
        consulta &= Q(tiempo_preparacion=tiempo_preparacion)
    
    # Filtrar las recetas utilizando la consulta construida
    recetas = Receta.objects.filter(consulta).distinct()
    
    return render(request, 'lista_recetas.html', {'recetas': recetas})
#endregion

#region CRUD CONSEJEROS
def Home_Administracion(request):
    return render(request, 'Home_Administracion.html')

def consejero_insertar(request):
    if request.method == "POST":
        if (
            request.POST.get('nombre') and
            request.POST.get('apellido') and
            request.POST.get('edad') and
            request.POST.get('idioma') and
            request.POST.get('fecha_nacimiento') and
            request.POST.get('titulacion') and
            request.POST.get('pais') and
            request.POST.get('experiencia')
        ):
            consejero = Consejero()
            consejero.nombre = request.POST.get('nombre')
            consejero.apellido = request.POST.get('apellido')
            consejero.edad = request.POST.get('edad')
            consejero.idioma = request.POST.get('idioma')
            consejero.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            consejero.titulacion = request.POST.get('titulacion')
            consejero.pais = request.POST.get('pais')
            consejero.experiencia = request.POST.get('experiencia')
            consejero.save()
            return redirect('/Administracion/Consejeros/listado')
    return render(request, "crud_consejeros/insertar.html")

def consejero_listado(request):
    consejeros = Consejero.objects.all()
    return render(request, 'crud_consejeros/listar.html', {'consejeros': consejeros})

def borrar_consejero(request, id_consejero):
    consejero = Consejero.objects.filter(id_consejero=id_consejero)
    consejero.delete()
    return redirect('/Administracion/Consejeros/listado')

def consejero_actualizar(request, id_consejero):
    if request.method == "POST":
        if (
            request.POST.get('nombre') and
            request.POST.get('apellido') and
            request.POST.get('edad') and
            request.POST.get('idioma') and
            request.POST.get('fecha_nacimiento') and
            request.POST.get('titulacion') and
            request.POST.get('pais') and
            request.POST.get('experiencia')
        ):
            consejero = Consejero.objects.get(pk=id_consejero)
            consejero.nombre = request.POST.get('nombre')
            consejero.apellido = request.POST.get('apellido')
            consejero.edad = request.POST.get('edad')
            consejero.idioma = request.POST.get('idioma')
            consejero.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            consejero.titulacion = request.POST.get('titulacion')
            consejero.pais = request.POST.get('pais')
            consejero.experiencia = request.POST.get('experiencia')
            consejero.save()
            return redirect('/Administracion/Consejeros/listado')
    else:
        consejero = Consejero.objects.filter(id_consejero=id_consejero)
        return render(request, "crud_consejeros/actualizar.html", {"consejeros": consejero})
#endregion