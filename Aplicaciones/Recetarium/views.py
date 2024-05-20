from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .models import Consejero, Receta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')

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

def soporte_tecnico(request):
    return render(request, 'soporte_tecnico.html')

def crear_elegir_receta(request):
    return render(request, 'crear_elegir_receta.html')

def invalid_page(request):
    return render(request, 'invalid_page.html')

# PÁGINA RECETAS DISPONIBLES
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

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
        if request.FILES.get('imagen') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('edad') and request.POST.get('idioma') and request.POST.get('fecha_nacimiento') and request.POST.get('titulacion') and request.POST.get('pais') and request.POST.get('experiencia'):
            insertar = connection.cursor()
            imagen = request.FILES.get('imagen')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            edad = request.POST.get('edad')
            idioma = request.POST.get('idioma')
            fecha_nacimiento = request.POST.get('fecha_nacimiento')
            titulacion = request.POST.get('titulacion')
            pais = request.POST.get('pais')
            experiencia = request.POST.get('experiencia')
            fs = FileSystemStorage()
            filename = fs.save(imagen.name, imagen)
            imagen_path = fs.url(filename)
            insertar.execute("call insertarconsejeros(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (imagen_path, nombre, apellido, edad, idioma, fecha_nacimiento, titulacion, pais, experiencia))
            return redirect('/Administracion/Consejeros/listado')
        else:
            return render(request, 'crud_consejeros/insertar.html')
    else:
        return render(request, 'crud_consejeros/insertar.html')

def consejero_listado(request):
    query = request.GET.get('q', '')
    page_number = request.GET.get('page', 1)  # Obtiene el número de página, si no hay, es la primera página.

    with connection.cursor() as cursor:
        if query:
            sql_query = """
                SELECT * FROM tbl_consejeros
                WHERE nombre LIKE %s
                OR apellido LIKE %s
                OR titulacion LIKE %s
                OR pais LIKE %s
            """
            cursor.execute(sql_query, [f'%{query}%', f'%{query}%', f'%{query}%', f'%{query}%'])
        else:
            cursor.execute('CALL listadoconsejeros()')
        
        consejeros = cursor.fetchall()
    
    # Crear un objeto Paginator con los resultados y el número deseado de elementos por página.
    paginator = Paginator(consejeros, 15)
    page_obj = paginator.get_page(page_number)  # Obtener la página solicitada.

    return render(request, 'crud_consejeros/listar.html', {'consejeros': page_obj, 'query': query})

def borrar_consejero(request,idconsejeros):
    borrar = connection.cursor()
    borrar.execute("call borrarconsejeros('"+str(idconsejeros)+"')")
    return redirect('/Administracion/Consejeros/listado')

def consejero_actualizar(request, idconsejeros):
    if request.method == "POST":
        imagen_nueva = request.FILES.get('imagen')
        if all([request.POST.get('nombre'), request.POST.get('apellido'), request.POST.get('edad'), request.POST.get('idioma'), request.POST.get('fecha_nacimiento'), request.POST.get('titulacion'), request.POST.get('pais'), request.POST.get('experiencia')]):
            insertar = connection.cursor()
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            edad = request.POST.get('edad')
            idioma = request.POST.get('idioma')
            fecha_nacimiento = request.POST.get('fecha_nacimiento')
            titulacion = request.POST.get('titulacion')
            pais = request.POST.get('pais')
            experiencia = request.POST.get('experiencia')
            if imagen_nueva:
                fs = FileSystemStorage()
                filename = fs.save(imagen_nueva.name, imagen_nueva)
                imagen_path = fs.url(filename)
            else:
                # Si no se cargó una nueva imagen, utiliza la imagen existente en la base de datos
                unconsejero = connection.cursor()
                unconsejero.execute("CALL consultarunconsejero(%s)", [idconsejeros])
                consejero = unconsejero.fetchone()
                imagen_path = consejero[1]
            insertar.execute("CALL actualizarconsejeros(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (idconsejeros, imagen_path, nombre, apellido, edad, idioma, fecha_nacimiento, titulacion, pais, experiencia))
            return redirect('/Administracion/Consejeros/listado')
    else:
        unconsejero = connection.cursor()
        unconsejero.execute("CALL consultarunconsejero(%s)", [idconsejeros])
        consejero = unconsejero.fetchone()
        return render(request, 'crud_consejeros/actualizar.html', {"consejero": consejero})
    
def mostrar_imagen_grande(request, imagen_url):
    return render(request, 'mostrar_imagen_grande.html', {'imagen_url': imagen_url})
    
#endregion