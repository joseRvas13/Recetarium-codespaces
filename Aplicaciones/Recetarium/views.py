from django.contrib import messages
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import (
    ConsejeroForm,
    CustomUserCreationForm,
    BMICalculatorForm,
    DietaForm,
    IngredienteForm,
    RecetaForm,
)
from .models import Consejero, Dieta, Ingrediente, Receta, Rol
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from django.core.mail import send_mail
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse



# region INDEX Y 404


def Not_Found(request):
    pagina_actual = "Not_Found"
    return render(request, "404.html", {"pagina": pagina_actual})

def index(request):
    return render(request, "index.html")


def bienvenido(request):
    pagina_actual = "bienvenido" 
    return render(request, "recetarium.html", {"pagina": pagina_actual})




# endregion


def informacion(request):
    pagina_actual = "informacion" 
    return render(request, "informacion.html", {"pagina": pagina_actual})


def olvido_contraseña(request):
    pagina_actual = "olvido_contraseña"
    return render(request, "Olvido_Contraseña.html", {"pagina": pagina_actual})


def salud_nutricion(request):
    pagina_actual = "salud_nutricion"
    return render(request, "salud_nutricion.html", {"pagina": pagina_actual})


def plan_nutricional(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    pagina_actual = "plan_nutricional"
    return render(request, "Usuarios/plan_nutricional.html", {"pagina": pagina_actual})


# region SOPORTE TECNICO


def soporte_tecnico(request):
    pagina_actual = "soporte_tecnico"

    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        email = request.POST.get("email")

        # Validar si la descripción no está vacía
        if descripcion and email:
            # Enviar correo
            send_mail(
                "Nuevo problema reportado",
                f"Descripción del problema:\n{descripcion}\n\nCorreo del remitente:\n{email}",
                settings.DEFAULT_FROM_EMAIL,
                ["recetarium19@gmail.com"],
                fail_silently=False,
            )
            # Mostrar mensaje de éxito
            messages.success(
                request,
                "Tu solicitud ha sido enviada correctamente. Nos pondremos en contacto contigo pronto.",
            )
            # Redirigir a una página de confirmación o regresar al formulario (según el flujo de tu aplicación)
            return redirect("soporte_send")
        else:
            # Mostrar mensaje de error si la descripción o el email están vacíos
            messages.error(
                request, "Por favor proporciona una descripción del problema y tu correo electrónico."
            )

    # Renderizar la plantilla del formulario
    return render(request, "soporte.html", {"pagina_actual": pagina_actual})
    # Renderizar el formulario inicial si no es método POST o si hay errores


def soporte_send(request):
    pagina_actual = "soporte_send"
    return render(request, "Soporte/soporte_send.html", {"pagina": pagina_actual})


# end
    

def home(request):
    return render(request, "index.html")



# region CONSEJEROS DISPONIBLES

def lista_consejeros(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    pagina_actual = "lista_consejeros"
    consejeros_list = Consejero.objects.all().order_by(
        "id_consejero"
    ) 
    consejeros_por_pagina = 9
    paginator = Paginator(consejeros_list, consejeros_por_pagina)

    page = request.GET.get("page")
    try:
        consejeros = paginator.page(page)
    except PageNotAnInteger:
        consejeros = paginator.page(1)
    except EmptyPage:
        consejeros = paginator.page(paginator.num_pages)

    return render(
        request,
        "Consejeros/lista_consejeros.html",
        {"consejeros": consejeros, "pagina": pagina_actual},
    )


# endregion


# region  RECETAS DISPONIBLES
def lista_recetas(request):
    pagina_actual = "lista_recetastas"
    recetas_list = Receta.objects.all()
    recetas_por_pagina = 21
    paginator = Paginator(recetas_list, recetas_por_pagina)
    page_number = request.GET.get("page")

    # Verificar si el parámetro de página está presente
    if page_number is None:
        # Si no hay parámetro de página, redirigir a la primera página
        return render(request, "Recetas/lista_recetas.html", {"recetas": paginator.page(1)})

    try:
        recetas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error
    except EmptyPage:
        # Si el número de página está fuera del rango, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error

    return render(request, "Recetas/lista_recetas.html", {"recetas": recetas , "pagina": pagina_actual})

def detalle_receta(request, id_receta):
    pagina_actual = "detalle_receta"
    receta = Receta.objects.get(pk=id_receta)
    return render(request, "Recetas/detalle_receta.html", {"receta": receta, "pagina": pagina_actual})

def buscar_recetas(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    query = request.GET.get("search")
    categoria = request.GET.get("categoria")
    dificultad = request.GET.get("dificultad")
    tiempo_preparacion = request.GET.get("tiempo_preparacion")

    # Eliminar caracteres no alfabéticos de la consulta
    query = re.sub(r"[^a-zA-Z\s]", "", query) if query else None

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

    return render(request, "Recetas/lista_recetas.html", {"recetas": recetas})

@login_required
def receta_crear(request):
    pagina_actual = "receta_crear"
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_plato = request.POST.get('nombre_plato')
        categoria = request.POST.get('categoria')
        temporada = request.POST.get('temporada')
        origen = request.POST.get('origen')
        ingredientes = request.POST.get('ingredientes')
        descripcion = request.POST.get('descripcion')
        instrucciones = request.POST.get('instrucciones')
        tiempo_preparacion = request.POST.get('tiempo_preparacion')
        dificultad = request.POST.get('dificultad')
        imagen = request.FILES.get('imagen')  # Usar get para manejar el caso de que no haya imagen

        # Obtener el usuario actual
        usuario = request.user

        # Crear la nueva instancia de Receta
        nueva_receta = Receta(
            nombre_plato=nombre_plato,
            categoria=categoria,
            temporada=temporada,
            origen=origen,
            ingredientes=ingredientes,
            descripcion=descripcion,
            instrucciones=instrucciones,
            tiempo_preparacion=tiempo_preparacion,
            dificultad=dificultad,
            imagen=imagen,
            usuario=usuario  # Asignar el usuario actual
        )

        # Guardar la receta en la base de datos
        nueva_receta.save()
    
        return redirect('lista_recetas')
    else:
        # Manejar el caso de solicitud GET si es necesario
        return render(request, 'Recetas/receta_crear.html', {"pagina": pagina_actual})
    
def crear_elegir_receta(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    pagina_actual = "crear_elegir_receta"
    return render(request, "Recetas/Crear_Elegir_Receta.html", {"pagina": pagina_actual})



def ver_recetas_usuarios(request, usuario_id):
    user = get_object_or_404(User, id=usuario_id)
    recetas_usuario = Receta.objects.filter(usuario=user)
    return render(
        request,
        "Recetas/ver_recetas_usuarios.html",
        {"user": user, "recetas_usuario": recetas_usuario},
    )
# endregion

# region DIETAS DISPONIBLES 
def lista_dietas(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    pagina_actual = "lista_dietas"
    dietas_list = Dieta.objects.all()
    dietas_por_pagina = 15
    paginator = Paginator(dietas_list, dietas_por_pagina)
    page_number = request.GET.get("page")

    if page_number is None:
        # Si no hay parámetro de página, redirigir a la primera página
        page_number = 1

    try:
        dietas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la primera página
        dietas = paginator.page(1)
    except EmptyPage:
        # Si el número de página está fuera del rango, mostrar la última página
        dietas = paginator.page(paginator.num_pages)

    return render(request, "dietas_disponibles/lista_dietas.html", {
        "dietas": dietas,
        "pagina": pagina_actual,
    })

def buscar_dietas(request):
    query = request.GET.get("search_dietas")

    query = re.sub(r"[^a-zA-Z\s]", "", query) if query else None

    consulta = Q()
    if query:
        consulta &= Q(nombre__icontains=query)

    dietas = Dieta.objects.filter(consulta).distinct()

    return render(request, "dietas_disponibles/lista_dietas.html", {"dietas": dietas})


def detalle_dietas(request, id_dieta_c):
    pagina_actual = "detalle_dietas"
    dietas = Dieta.objects.get(pk=id_dieta_c)
    return render(request, "dietas_disponibles/detalle_dietas.html", {"dietas": dietas, "pagina": pagina_actual})

def consejeros_dietas(request):
    pagina_actual = "consejeros_dietas"
    return render(request, "dietas_disponibles/form_consejero.html", {"pagina": pagina_actual})


# endregion



# region CRUD CONSEJEROS

def crear_consejero(request):
    if request.method == 'POST':
        form = ConsejeroForm(request.POST, request.FILES)
        if form.is_valid():
            consejero = form.save(commit=False)  # Guardar el formulario sin commit
            consejero.habilitado = True  # Establecer como habilitado
            consejero.save()  # Guardar el consejero con la habilitación

            data = {
                'nombre': consejero.nombre,
                'apellido': consejero.apellido,
                'pais': consejero.pais,
                'experiencia': consejero.experiencia,
                'habilitado': consejero.habilitado,  # Incluir el estado de habilitación en la respuesta
            }
            return JsonResponse(data)  # Devuelve los datos del consejero en formato JSON
        else:
            # Manejar el caso cuando el formulario no es válido
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ConsejeroForm()

    return render(request, 'crud_consejeros/insertar.html', {'form': form})

def listar_consejeros(request):
    consejeros = Consejero.objects.order_by("-fecha_registro")

    # Filtrado por búsqueda
    query = request.GET.get("q")
    if query:
        consejeros = consejeros.filter(nombre__icontains=query)

    # Paginación
    paginator = Paginator(consejeros, 15)  # 15 consejeros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "consejeros": page_obj,  # Cambia a 'page_obj' para usar la paginación en la plantilla
        "query": query,
        "paginator": paginator,  # Incluye el paginador en el contexto
    }
    return render(request, "crud_consejeros/listar.html", context)


def actualizar_consejero(request, pk):
    consejero = get_object_or_404(Consejero, pk=pk)

    if request.method == "POST":
        form = ConsejeroForm(request.POST, request.FILES, instance=consejero)
        if form.is_valid():
            form.save()
            # Si el formulario se guarda correctamente, retorna un mensaje JSON
            return JsonResponse({'message': '¡Consejero actualizado correctamente!'})
        else:
            # Si hay errores en el formulario, retorna los errores
            return JsonResponse({'error': form.errors}, status=400)
    else:
        form = ConsejeroForm(instance=consejero)

    return render(
        request,
        "crud_consejeros/actualizar.html",
        {"form": form, "consejero": consejero},
    )


def consejeros_inhabilitados(request):
    consejeros = Consejero.objects.filter(status='inhabilitado')
    return render(request, 'crud_consejeros/listar.html', {'consejeros': consejeros})

def inhabilitar_consejero(request, pk):
    consejero = get_object_or_404(Consejero, pk=pk)
    
    if consejero.status == 'habilitado':
        consejero.status = 'inhabilitado'
        message = "Receta inhabilitada correctamente."
    else:
        consejero.status = 'habilitado'
        message = "Receta habilitada correctamente."
    
    consejero.save()
    
    return JsonResponse({'message': message})


def mostrar_imagen_grande(request, id_consejero):
    consejero = get_object_or_404(Consejero, id_consejero=id_consejero)
    context = {"consejero": consejero}
    return render(request, "crud_consejeros/mostrar_imagen_grande.html", context)


# endregion

# region CRUD RECETAS


def crear_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Receta creada exitosamente.'})
        else:
            # Recoge los errores del formulario para mostrarlos en el frontend
            errores = form.errors.as_json()
            return JsonResponse({'success': False, 'message': 'Por favor, corrija los errores a continuación.', 'errors': errores})
    else:
        form = RecetaForm()
    return render(request, "crud_recetas/insertar.html", {"form": form})


def listar_recetas(request):
    recetas = Receta.objects.all().order_by('-fecha_registro_receta')
    
    # Paginación
    paginator = Paginator(recetas, 15)  # 15 recetas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'recetas': page_obj,
        'paginator': paginator
    }
    return render(request, 'crud_recetas/listar.html', context)

def recetas_inhabilitadas(request):
    recetas = Receta.objects.filter(status='inhabilitado')
    return render(request, 'crud_recetas/listar.html', {'recetas': recetas})

def inhabilitar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    
    if receta.status == 'habilitado':
        receta.status = 'inhabilitado'
        message = "Receta inhabilitada correctamente."
    else:
        receta.status = 'habilitado'
        message = "Receta habilitada correctamente."
    
    receta.save()
    
    return JsonResponse({'message': message})


def actualizar_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)

    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            return redirect("listar_recetas")
    else:
        form = RecetaForm(instance=receta)

    return render(
        request, "crud_recetas/actualizar.html", {"form": form, "receta": receta}
    )


def ver_recetas(request, receta_id):
    receta = get_object_or_404(Receta, id_receta=receta_id)
    return render(request, "crud_recetas/ver_receta.html", {"receta": receta})


def ver_imagen(request, id_receta):
    receta = get_object_or_404(Receta, id_receta=id_receta)
    context = {"receta": receta}
    return render(request, "crud_recetas/ver_imagen.html", context)


# endregion

# region CRUD DIETAS

def crear_dietas(request):
    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_dieta = form.save(commit=False)
            consejero_id = form.cleaned_data["consejero_id"]
            usuario_id = form.cleaned_data["usuario_id"]
            nueva_dieta.consejero = consejero_id
            nueva_dieta.usuario = usuario_id
            nueva_dieta.save()
            response_data = {
                "success": True,
                "message": "Dieta creada exitosamente."
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                "success": False,
                "message": "Hubo un error al crear la dieta. Por favor, revise el formulario."
            }
            return JsonResponse(response_data, status=400)
    else:
        form = DietaForm()

    context = {
        "form": form,
    }
    return render(request, "crud_dietas/insertar.html", context)

def listar_dietas(request):

    dietas = Dieta.objects.select_related('consejero', 'usuario').all().order_by('-fecha_registro_dieta')

    # Paginación
    paginator = Paginator(dietas, 2)  # 15 dietas por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'dietas': page_obj,
        'paginator': paginator
    }

    return render(request, "crud_dietas/listar.html", context)


def actualizar_dietas(request, pk):
    dieta = get_object_or_404(Dieta, pk=pk)
    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES, instance=dieta)
        if form.is_valid():
            dieta = form.save(commit=False)

            if form.cleaned_data["usuario_id"] == "Sistema Recetarium":
                dieta.usuario_id = None
            else:
                dieta.usuario_id = form.cleaned_data["usuario_id"]

            if form.cleaned_data["consejero_id"] == "Sistema Recetarium":
                dieta.consejero_id = None
            else:
                dieta.consejero_id = form.cleaned_data["consejero_id"]

            dieta.save()
            return JsonResponse({"success": True, "message": "Dieta actualizada correctamente."})
        else:
            return JsonResponse({"success": False, "message": "Error al actualizar la dieta."})
    else:
        form = DietaForm(instance=dieta)

    return render(
        request, "crud_dietas/actualizar.html", {"form": form, "dieta": dieta}
    )

def dietas_inhabilitadas(request):
    dietas = Dieta.objects.filter(status='inhabilitado')
    return render(request, 'crud_dietas/listar.html', {'dietas': dietas})

def inhabilitar_dieta(request, pk):
    dieta = get_object_or_404(Dieta, pk=pk)
    
    if dieta.status == 'habilitado':
        dieta.status = 'inhabilitado'
        message = "Dieta inhabilitada correctamente."
    else:
        dieta.status = 'habilitado'
        message = "Dieta habilitada correctamente."
    
    dieta.save()
    
    return JsonResponse({'message': message})

def ver_dietas(request, dieta_id):
    dieta = get_object_or_404(Dieta, id_dieta_c=dieta_id)
    return render(request, "crud_dietas/ver_dietas.html", {"dieta": dieta})


def mostrar_imagen_grande_dieta(request, id_dieta_c):
    dieta = get_object_or_404(Dieta, id_dieta_c=id_dieta_c)
    context = {"dieta": dieta}
    return render(request, "crud_dietas/mostrar_imagen_grande_dieta.html", context)


# endregion

# region CRUD INGREDIENTES


def crear_ingrediente(request):
    if request.method == "POST":
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("listado_ingredientes"))
    else:
        form = IngredienteForm()

    context = {"form": form}
    return render(request, "crud_ingredientes/insertar.html", context)


def crud_listado_ingredientes(request):
    ingredientes_list = Ingrediente.objects.all().order_by('-fecha_registro_ingredientes')

    # Filtrar por búsqueda si hay parámetro 'q' en la URL
    query = request.GET.get("q")
    if query:
        ingredientes_list = ingredientes_list.filter(nombre__icontains=query)

    # Configurar paginación
    paginator = Paginator(ingredientes_list, 15)  # 15 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "ingredientes": page_obj,
        "query": query,
    }
    return render(request, "crud_ingredientes/listar.html", context)


def actualizar_ingrediente(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == "POST":
        form = IngredienteForm(request.POST, instance=ingrediente)
        if form.is_valid():
            form.save()
            return redirect("listado_ingredientes")
    else:
        form = IngredienteForm(instance=ingrediente)

    return render(
        request,
        "crud_ingredientes/actualizar.html",
        {"form": form, "ingrediente": ingrediente},
    )


def borrar_ingrediente(request, pk):
    # Obtener el ingrediente o devolver un error 404 si no existe
    ingrediente = get_object_or_404(Ingrediente, pk=pk)

    if request.method == "POST":
        # Si la solicitud es POST, se está confirmando la eliminación
        ingrediente.delete()
        messages.success(request, "¡El ingrediente ha sido eliminado correctamente!")
        return JsonResponse({'message': '¡El ingrediente ha sido eliminado correctamente!'}, status=200)
    else:
        # Manejar otras solicitudes como GET si es necesario
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def ver_ingrediente(request, ingrediente_id):
    ingrediente = get_object_or_404(Ingrediente, id_ingrediente=ingrediente_id)
    return render(
        request, "crud_ingredientes/ver_ingrediente.html", {"ingrediente": ingrediente}
    )


# endregion


# region CRUD ROLES
def insertar_roles(request):
    if request.method == "POST":
        if (
            request.POST.get("nombre")
            and request.POST.get("descripcion")
            and request.POST.get("permisos")
        ):
            roles = Rol()
            roles.nombre = request.POST.get("nombre")
            roles.descripcion = request.POST.get("descripcion")
            roles.permisos = request.POST.get("permisos")
            roles.save()
            return redirect("/administracion/roles/listado")
        else:
            return render(request, "crud_roles/insertar.html")
    else:
        return render(request, "crud_roles/insertar.html")


def listado_roles(request):
    roles = Rol.objects.all()
    return render(request, "crud_roles/listar.html", {"roles": roles})


def borrar_rol(request, idroles):
    roles = Rol.objects.filter(id=idroles)
    roles.delete()
    return redirect("/administracion/roles/listado")


def actualizar_rol(request, idroles):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        permisos = request.POST.get("permisos")

        if nombre and descripcion and permisos:
            roles = Rol.objects.get(id=idroles)
            roles.nombre = nombre
            roles.descripcion = descripcion
            roles.permisos = permisos
            roles.save()
            return redirect("/administracion/roles/listado")
    else:
        roles = Rol.objects.get(id=idroles)
        return render(request, "crud_roles/actualizar.html", {"roles": roles})


# endregion


# region CALCULADORA IMC


def calculadoraB(request):
    pagina_actual = "calcualdoraB"
    return render(request, "Calculadora/Calculadora.html", {"pagina": pagina_actual})


# endregion


# region INICIO SESION , REGISTRO , LOGOUT , USUARIOS
def registro_usuario(request):
    pagina_actual = "registro"
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmar_contraseña = request.POST.get("confirmar_contraseña")

        # Validar que todos los campos requeridos estén presentes y las contraseñas coincidan
        if username and email and password and password == confirmar_contraseña:
            # Verificar si el correo electrónico ya está en uso
            if User.objects.filter(email=email).exists():
                messages.error(
                    request,
                    "El correo electrónico ya está en uso. Por favor, utiliza otro.",
                )
                return render(
                    request, "Usuarios/registro.html", {"pagina": pagina_actual}
                )
            else:
                try:
                    # Crear el usuario si el correo electrónico es único
                    user = User.objects.create_user(
                        username=username, email=email, password=password
                    )
                    user.save()
                    messages.success(
                        request, "¡Registro exitoso! Ahora puedes iniciar sesión."
                    )
                    return redirect("/Usuarios/login")
                except Exception as e:
                    messages.error(request, f"Error al crear usuario: {e}")
                    return render(
                        request, "Usuarios/registro.html", {"pagina": pagina_actual}
                    )
        else:
            # Si los campos no están completos o las contraseñas no coinciden, mostrar el formulario nuevamente con un mensaje de error
            messages.error(
                request,
                "Por favor, completa todos los campos y asegúrate de que las contraseñas coincidan.",
            )
            return render(request, "Usuarios/registro.html", {"pagina": pagina_actual})

    # Si la solicitud no es POST, renderizar el formulario vacío
    return render(request, "Usuarios/registro.html", {"pagina": pagina_actual})

def loginusuarios(request):
    pagina_actual = "loginusuarios"
    mensaje = ""

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                # Buscar el usuario por correo electrónico
                user = User.objects.get(email=email)
                # Autenticar utilizando el nombre de usuario del usuario encontrado
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('principal_usuario')
                else:
                    mensaje = "Usuario o Contraseña incorrectos, Intente de nuevo"  
            except User.DoesNotExist:
                mensaje = "Usuario o Contraseña incorrectos, Intente de nuevo"
        else:
            mensaje = "Por favor, ingrese ambos campos"

    return render(request, "Usuarios/login.html", {"pagina": pagina_actual, "mensaje": mensaje})
    
@login_required
def principal_usuario(request):
    pagina_actual = "principal_usuario"
    return render(request, "Usuarios/principal_usuario.html", {"pagina": pagina_actual})

@login_required
def perfil_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    return render(request, 'Usuarios/usuario.html', {'usuario': usuario})

@login_required
def usuario(request, user_id):
    pagina_actual = "usuario"
    usuario = get_object_or_404(User, id=user_id)
    return render(request, "Usuarios/usuario.html", {'usuario': usuario ,"pagina": pagina_actual})

def logoutusuarios(request):
    logout(request)
    return redirect('/')

@login_required
def perfil_config(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    return render(request, 'Usuarios/config.html', {'usuario': usuario})
# endregion


# region PANEL ADMINISTRATIVO


def Home_Administracion(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    return render(request, "Administracion/Home_Administracion.html")


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("/Usuarios/login")
    total_usuarios = User.objects.count()
    total_consejeros = Consejero.objects.count()
    total_recetas = Receta.objects.count()
    total_dietas = Dieta.objects.count()
    total_ingredientes = Ingrediente.objects.count()
    total_roles = Rol.objects.count()
    consejeros_recientes = Consejero.objects.order_by("-fecha_registro")[:3]

    context = {
        "total_usuarios": total_usuarios,
        "total_consejeros": total_consejeros,
        "total_recetas": total_recetas,
        "total_dietas": total_dietas,
        "total_ingredientes": total_ingredientes,
        "total_roles": total_roles,
        "consejeros_recientes": consejeros_recientes,
    }

    consejeros_recientes = Consejero.objects.order_by('-fecha_registro')[:3]
    recetas_recientes = Receta.objects.order_by('-fecha_registro_receta')[:3]
    dietas_recientes = Dieta.objects.order_by('-fecha_registro_dieta')[:3]
    ingredientes_recientes = Ingrediente.objects.order_by('-fecha_registro_ingredientes')[:3]


    context = {
        'total_usuarios': total_usuarios,
        'total_consejeros': total_consejeros,
        'total_recetas': total_recetas,
        'total_dietas': total_dietas,
        'total_ingredientes': total_ingredientes,
        'total_roles': total_roles,

        'consejeros_recientes': consejeros_recientes,
        'recetas_recientes': recetas_recientes,
        'dietas_recientes': dietas_recientes,
        'ingredientes_recientes': ingredientes_recientes,
    }

    return render(request, 'Home_Administracion.html', context)


# endregion

