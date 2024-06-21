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
from django.shortcuts import render, get_object_or_404
from django.conf import settings


# region INDEX


def index(request):
    return render(request, "index.html")


def bienvenido(request):
    return render(request, "recetarium.html")


# endregion


def informacion(request):
    return render(request, "informacion.html")


def crear_elegir_receta(request):
    pagina_actual = "crear_elegir_receta"
    return render(request, "Crear_Elegir_Receta.html")


def olvido_contraseña(request):
    pagina_actual = "olvido_contraseña"
    return render(request, "Olvido_Contraseña.html")


def salud_nutricion(request):
    pagina_actual = "salud_nutricion"
    return render(request, "salud_nutricion.html", {"pagina": pagina_actual})


def plan_nutricional(request):
    pagina_actual = "plan_nutricional"
    return render(request, "plan_nutricional.html", {"pagina": pagina_actual})


# region SOPORTE TECNICO


def soporte_tecnico(request):
    pagina_actual = "soporte_tecnico"

    if request.method == "POST":
        descripcion = request.POST.get("descripcion")

        # Validar si la descripción no está vacía
        if descripcion:
            # Enviar correo
            send_mail(
                "Nuevo problema reportado",
                f"Descripción del problema:\n{descripcion}",
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
            return redirect("/")
        else:
            # Mostrar mensaje de error si la descripción está vacía
            messages.error(
                request, "Por favor proporciona una descripción del problema."
            )

    # Renderizar el formulario inicial si no es método POST o si hay errores
    return render(request, "Soporte/soporte.html", {"pagina": pagina_actual})


def soporte_send(request):
    pagina_actual = "soporte_send"
    return render(request, "Soporte/soporte_send.html", {"pagina": pagina_actual})


# end

# region 404


def Not_Found(request):
    pagina_actual = "Not_Found"
    return render(request, "404.html", {"pagina": pagina_actual})


# endrefion


# region FORMULARIO DE CREAR RECETAS (USUARIO)
def receta_crear(request):
    pagina_actual = "receta_crear"
    return render(request, "receta_crear.html", {"pagina": pagina_actual})


# endregion


def invalid_page(request):
    return render(request, "invalid_page.html")


# PÁGINA RECETAS DISPONIBLES
def lista_recetas(request):
    pagina_actual = "lista_recetas"
    recetas = Receta.objects.all()
    return render(
        request, "lista_recetas.html", {"recetas": recetas, "pagina": pagina_actual}
    )


def lista_consejeros(request):
    consejeros = Consejero.objects.all()
    return render(request, "lista_consejeros.html", {"consejeros": consejeros})


# region paginacion consejeros
def lista_consejeros(request):
    pagina_actual = "lista_consejeros"
    consejeros_list = Consejero.objects.all().order_by(
        "id_consejero"
    )  # Asegúrate de que el nombre del modelo es Consejero
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
        "lista_consejeros.html",
        {"consejeros": consejeros, "pagina": pagina_actual},
    )


# endregion


# region PÁGINA DETALLES DE LAS RECETAS POR SU ID
def detalle_receta(request, id_receta):
    receta = Receta.objects.get(pk=id_receta)
    return render(request, "detalle_receta.html", {"receta": receta})


# endregion


# region PÁGINACION RECETAS DISPONIBLES
def lista_recetas(request):
    recetas_list = Receta.objects.all()
    recetas_por_pagina = 21
    paginator = Paginator(recetas_list, recetas_por_pagina)
    page_number = request.GET.get("page")

    # Verificar si el parámetro de página está presente
    if page_number is None:
        # Si no hay parámetro de página, redirigir a la primera página
        return render(request, "lista_recetas.html", {"recetas": paginator.page(1)})

    try:
        recetas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error
    except EmptyPage:
        # Si el número de página está fuera del rango, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error

    return render(request, "lista_recetas.html", {"recetas": recetas})


# endregion


# region SIGNUP USUARIO, LOGIN , LOGOUT ,REGISTER
def Registro(request):
    pagina_actual = "Registro"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Verificar si el correo electrónico ya existe en la base de datos
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                # Si el correo electrónico ya existe, mostrar un mensaje de error
                return render(
                    request,
                    "registro.html",
                    {
                        "form": form,
                        "error_message": "El correo electrónico ya está en uso. Por favor, utiliza otro.",
                    },
                )
            else:
                # Si el correo electrónico es único, guardar el formulario y crear el usuario
                form.save()
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password1"]
                user = authenticate(request, email=email, password=password)
                login(request, user)
                # No establecer signup_success en la sesión aquí
                return redirect(
                    "/"
                )  # Redirigir a la página de éxito después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, "Registro.html", {"form": form, "pagina": pagina_actual})


def home(request):
    return render(request, "index.html")


# endregion


# region FUNCIONALIAD BUSQUEDA DE RECETAS (RECETAS DISPONIBLES)
def buscar_recetas(request):
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

    return render(request, "lista_recetas.html", {"recetas": recetas})


# endregion

# region DIETAS DISPONIBLES - CALENDARIO


def lista_dietas(request):
    dietas = Dieta.objects.all()
    return render(request, "dietas_disponibles/lista_dietas.html", {"dietas": dietas})


def lista_dietas(request):
    dietas_list = Dieta.objects.all()
    dietas_por_pagina = 15
    paginator = Paginator(dietas_list, dietas_por_pagina)
    page_number = request.GET.get("page")

    # Verificar si el parámetro de página está presente
    if page_number is None:
        # Si no hay parámetro de página, redirigir a la primera página
        return render(
            request,
            "dietas_disponibles/lista_dietas.html",
            {"dietas": paginator.page(1)},
        )

    try:
        dietas = paginator.page(page_number)
    except PageNotAnInteger:
        # Si el número de página no es un entero, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error
    except EmptyPage:
        # Si el número de página está fuera del rango, mostrar la página de error personalizada
        return render(request, "invalid_page.html")  # Redirigir a la página de error

    return render(request, "dietas_disponibles/lista_dietas.html", {"dietas": dietas})


def buscar_dietas(request):
    query = request.GET.get("search_dietas")

    query = re.sub(r"[^a-zA-Z\s]", "", query) if query else None

    consulta = Q()
    if query:
        consulta &= Q(nombre__icontains=query)

    dietas = Dieta.objects.filter(consulta).distinct()

    return render(request, "dietas_disponibles/lista_dietas.html", {"dietas": dietas})


def detalle_dietas(request, id_dieta_c):
    dietas = Dieta.objects.get(pk=id_dieta_c)
    return render(request, "dietas_disponibles/detalle_dietas.html", {"dietas": dietas})


# endregion

# region VER RECETAS POR EL ID DEL USUARIO


def ver_recetas_usuarios(request, usuario_id):
    user = get_object_or_404(User, id=usuario_id)
    recetas_usuario = Receta.objects.filter(usuario=user)
    return render(
        request,
        "ver_recetas_usuarios/ver_recetas_usuarios.html",
        {"user": user, "recetas_usuario": recetas_usuario},
    )


# endregion


# region CRUD CONSEJEROS


def crear_consejero(request):
    if request.method == "POST":
        form = ConsejeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Consejero creado exitosamente.")
            return redirect("listar_consejeros")
        else:
            messages.error(request, "Por favor, corrija los errores a continuación.")
    else:
        form = ConsejeroForm()
    return render(request, "crud_consejeros/insertar.html", {"form": form})


def listar_consejeros(request):
    consejeros = Consejero.objects.all().order_by("-fecha_registro")

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
            messages.success(
                request, "¡El consejero ha sido actualizado correctamente!"
            )
            return redirect("listar_consejeros")
    else:
        form = ConsejeroForm(instance=consejero)

    return render(
        request,
        "crud_consejeros/actualizar.html",
        {"form": form, "consejero": consejero},
    )


def borrar_consejero(request, pk):
    # Obtener el consejero o devolver un error 404 si no existe
    consejero = get_object_or_404(Consejero, pk=pk)

    if request.method == "POST":
        # Si la solicitud es POST, se está confirmando la eliminación
        consejero.delete()
        messages.success(request, "¡El consejero ha sido eliminado correctamente!")
        return redirect("listar_consejeros")

    # Si la solicitud no es POST, mostrar la página de confirmación de eliminación
    return render(request, "crud_consejeros/borrar.html", {"consejero": consejero})


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
            messages.success(request, "Receta creada exitosamente.")
            return redirect("listar_recetas")
        else:
            messages.error(request, "Por favor, corrija los errores a continuación.")
    else:
        form = RecetaForm()
    return render(request, "crud_recetas/insertar.html", {"form": form})


def listar_recetas(request):
    recetas = Receta.objects.all()
    context = {"recetas": recetas}
    return render(request, "crud_recetas/listar.html", context)

    recetas = Receta.objects.all().order_by('-fecha_registro_receta')
    context = {
        'recetas': recetas
    }
    return render(request, 'crud_recetas/listar.html', context)

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


def borrar_receta(request, pk):
    # Obtener la receta o devolver un error 404 si no existe
    receta = get_object_or_404(Receta, pk=pk)

    if request.method == "POST":
        # Si la solicitud es POST, se está confirmando la eliminación
        receta.delete()
        messages.success(request, "¡La receta ha sido eliminada correctamente!")
        return redirect("listar_recetas")

    # Si la solicitud no es POST, mostrar la página de confirmación de eliminación
    return render(request, "crud_recetas/borrar.html", {"receta": receta})


def ver_recetas(request, receta_id):
    receta = get_object_or_404(Receta, id_receta=receta_id)
    return render(request, "crud_recetas/ver_receta.html", {"receta": receta})


def ver_imagen(request, id_receta):
    receta = get_object_or_404(Receta, id_receta=id_receta)
    context = {"receta": receta}
    return render(request, "ver_imagen.html", context)


# endregion

# region CRUD DIETAS


def crear_dietas(request):
    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES)
        if form.is_valid():
            # Guarda la instancia de Dieta sin commit para poder asignar consejero y usuario manualmente
            nueva_dieta = form.save(commit=False)

            # Asigna el consejero y usuario seleccionados desde el formulario
            consejero_id = form.cleaned_data["consejero_id"]
            usuario_id = form.cleaned_data["usuario_id"]

            # Asigna los objetos correspondientes a los campos de la dieta
            nueva_dieta.consejero = consejero_id
            nueva_dieta.usuario = usuario_id

            # Guarda la dieta completa con los campos actualizados
            nueva_dieta.save()
            messages.success(request, "Dieta creada exitosamente.")
            return redirect(
                "listar_dietas"
            )  # Redirige a la vista de listado de dietas después de guardar
    else:
        form = DietaForm()

    context = {
        "form": form,
    }
    return render(request, "crud_dietas/insertar.html", context)


def listar_dietas(request):

    dietas = Dieta.objects.select_related('consejero', 'usuario').all().order_by('-fecha_registro_dieta')

    # Manejo de búsqueda
    query = request.GET.get("q")
    if query:
        dietas = dietas.filter(nombre__icontains=query)

    # Paginación
    paginator = Paginator(dietas, 15)  # Mostrar 15 registros por página
    page = request.GET.get("page")
    try:
        dietas_pagina = paginator.page(page)
    except PageNotAnInteger:
        dietas_pagina = paginator.page(1)
    except EmptyPage:
        dietas_pagina = paginator.page(paginator.num_pages)

    context = {
        "dietas": dietas_pagina,
        "query": query,  # Para mantener el valor de búsqueda en el formulario
    }
    return render(request, "crud_dietas/listar.html", context)


def actualizar_dietas(request, pk):
    dieta = get_object_or_404(Dieta, pk=pk)

    if request.method == "POST":
        form = DietaForm(request.POST, request.FILES, instance=dieta)
        if form.is_valid():
            # Guardar los cambios en la instancia de Dieta
            dieta = form.save(commit=False)

            # Actualizar usuario_id si se seleccionó uno nuevo
            if form.cleaned_data["usuario_id"] == "Sistema Recetarium":
                dieta.usuario_id = None
            else:
                dieta.usuario_id = form.cleaned_data["usuario_id"]

            # Actualizar consejero_id si se seleccionó uno nuevo
            if form.cleaned_data["consejero_id"] == "Sistema Recetarium":
                dieta.consejero_id = None
            else:
                dieta.consejero_id = form.cleaned_data["consejero_id"]

            dieta.save()
            return redirect("listar_dietas")
    else:
        form = DietaForm(instance=dieta)

    return render(
        request, "crud_dietas/actualizar.html", {"form": form, "dieta": dieta}
    )


def borrar_dietas(request, pk):
    # Obtener la receta o devolver un error 404 si no existe
    dieta = get_object_or_404(Dieta, pk=pk)

    if request.method == "POST":
        # Si la solicitud es POST, se está confirmando la eliminación
        dieta.delete()
        messages.success(request, "¡La dieta ha sido eliminada correctamente!")
        return redirect("listar_dietas")

    # Si la solicitud no es POST, mostrar la página de confirmación de eliminación
    return render(request, "crud_dietas/borrar.html", {"dieta": dieta})


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
        return redirect("listado_ingredientes")

    # Si la solicitud no es POST, mostrar la página de confirmación de eliminación
    return render(
        request, "crud_ingredientes/borrar.html", {"ingrediente": ingrediente}
    )


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


def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters**2)
    return bmi


def bmi_result(bmi):
    if bmi < 18.5:
        return "Bajo peso"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"


def bmi_calculator(request):
    pagina_actual = "bmi_calculator"
    if request.method == "POST":
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data["weight"]
            height = form.cleaned_data["height"]
            bmi = calculate_bmi(weight, height)
            result = bmi_result(bmi)
            return render(
                request, "result_calculadora.html", {"bmi": bmi, "result": result}
            )
    else:
        form = BMICalculatorForm()
    return render(
        request, "Calculadora_De_Salud.html", {"form": form, "pagina": pagina_actual}
    )


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
    if request.method == "POST":
        if request.POST.get("username") and request.POST.get("password"):
            user = authenticate(
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect("/home")
            else:
                mensaje = "Usuario o Contraseña incorrectos, Intente de nuevo"
                return render(request, "Usuarios/login.html", {"mensaje": mensaje})
    else:
        return render(request, "Usuarios/login.html")


def usuario(request):
    return render(request, "Usuarios/usuario.html")

# endregion

# region PANEL ADMINISTRATIVO


def Home_Administracion(request):
    return render(request, "Home_Administracion.html")


def dashboard(request):
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

    return render(request, "Home_Administracion.html", context)
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
