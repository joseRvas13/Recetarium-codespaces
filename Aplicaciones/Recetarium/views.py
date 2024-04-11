from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

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
