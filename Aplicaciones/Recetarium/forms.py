from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Consejero, Dieta, Ingrediente, Receta

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]  # Utiliza el correo electrónico como nombre de usuario
        if commit:
            user.save()
        return user
    
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class BMICalculatorForm(forms.Form):
    weight = forms.FloatField(label='Peso (kg)')
    height = forms.FloatField(label='Altura (cm)')  

#CRUD INGREDIENTES
class IngredienteForm(forms.ModelForm):
    receta = forms.ModelChoiceField(
        queryset=Receta.objects.all(),
        required=False,
        label="Receta",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Ingrediente
        fields = ['nombre', 'descripcion', 'cantidad', 'variedad', 'usos', 'p_nutricional', 'consejos', 'grasas_saturadas', 'calorias', 'hidratos_de_carbono', 'grasas_trans', 'total_carbohidratos', 'azucares', 'precio', 'receta']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'variedad': forms.TextInput(attrs={'class': 'form-control'}),
            'usos': forms.TextInput(attrs={'class': 'form-control'}),
            'p_nutricional': forms.TextInput(attrs={'class': 'form-control'}),
            'consejos': forms.TextInput(attrs={'class': 'form-control'}),
            'grasas_saturadas': forms.NumberInput(attrs={'class': 'form-control'}),
            'calorias': forms.NumberInput(attrs={'class': 'form-control'}),
            'hidratos_de_carbono': forms.NumberInput(attrs={'class': 'form-control'}),
            'grasas_trans': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_carbohidratos': forms.NumberInput(attrs={'class': 'form-control'}),
            'azucares': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receta'].queryset = Receta.objects.all()
        self.fields['receta'].label_from_instance = lambda obj: f'{obj.id_receta} - {obj.nombre_plato}'

#FIN CRUD INGREDIENTES

#CRUD RECETAS

class RecetaForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    imagen = forms.ImageField(
        required=True,
        label="Imagen",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = Receta
        fields = ['nombre_plato', 'imagen', 'categoria', 'temporada', 'origen', 'ingredientes', 'descripcion', 'instrucciones', 'tiempo_preparacion', 'dificultad', 'usuario']
        widgets = {
            'nombre_plato': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'temporada': forms.TextInput(attrs={'class': 'form-control'}),
            'origen': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'instrucciones': forms.TextInput(attrs={'class': 'form-control'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'dificultad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].queryset = User.objects.all()
        self.fields['usuario'].label_from_instance = lambda obj: f'{obj.id} - {obj.first_name} - {obj.last_name}'

#FIN CRUD RECETAS

#CRUD CONSEJEROS

class ConsejeroForm(forms.ModelForm):

    class Meta:
        model = Consejero
        fields = ['imagen', 'nombre', 'apellido', 'edad', 'descripcion', 'idioma', 'fecha_nacimiento', 'titulacion', 'pais', 'experiencia']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'idioma': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'titulacion': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'experiencia': forms.TextInput(attrs={'class': 'form-control'}),
        }

#endregion

#CRUD DIETAS

class DietaForm(forms.ModelForm):
    usuario_id = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label='Sistema Recetarium',
        label="Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    consejero_id = forms.ModelChoiceField(
        queryset=Consejero.objects.all(),
        required=False,
        empty_label='Sistema Recetarium',
        label="Consejero",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Dieta
        fields = ['nombre', 'descripcion', 'objetivo', 'calorias', 'condicion_medica',
                  'valor_nutricional', 'actividad_fisica', 'consejos', 'dispositivos',
                  'usuario_id', 'consejero_id', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'objetivo': forms.TextInput(attrs={'class': 'form-control'}),
            'calorias': forms.NumberInput(attrs={'class': 'form-control'}),
            'condicion_medica': forms.TextInput(attrs={'class': 'form-control'}),
            'valor_nutricional': forms.NumberInput(attrs={'class': 'form-control'}),
            'actividad_fisica': forms.TextInput(attrs={'class': 'form-control'}),
            'consejos': forms.TextInput(attrs={'class': 'form-control'}),
            'dispositivos': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario_id': forms.Select(attrs={'class': 'form-control'}),
            'consejero_id': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario_id'].queryset = User.objects.all()
        self.fields['usuario_id'].label_from_instance = lambda obj: f'{obj.first_name} {obj.last_name}'
        self.fields['usuario_id'].empty_label = 'Sistema Recetarium'
        self.fields['consejero_id'].queryset = Consejero.objects.all()
        self.fields['consejero_id'].label_from_instance = lambda obj: f'{obj.nombre} {obj.apellido}'
        self.fields['consejero_id'].empty_label = 'Sistema Recetarium'


