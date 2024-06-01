from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import Home_Administracion, actualizar_rol, borrar_consejero, borrar_rol, buscar_dietas, consejero_actualizar, consejero_insertar, consejero_listado, insertar_roles, lista_dietas, lista_recetas, buscar_recetas, listado_roles, receta_crear, lista_consejeros

urlpatterns = [
    path('', views.index, name="index"),
    path('eleccion-ver-crear-receta/', views.crear_elegir_receta, name='crear_elegir_receta'),
    path('recuperacion-de-contraseña/', views.olvido_contraseña, name="olvido_contraseña"),
    path('salud-nutricion/', views.salud_nutricion, name="salud_nutricion"),
    path('calculadora-salud/', views.calculadora_salud, name="calculadora_salud"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('soporte-tecnico/', views.soporte_tecnico, name='soporte_tecnico'),
    path('recetas/', lista_recetas, name='lista_recetas'),
    path('detalle_receta/<int:id_receta>/', views.detalle_receta, name='detalle_receta'),
    path('invalid_page/', views.invalid_page, name='invalid_page'),
    path('buscar/', buscar_recetas, name='buscar_recetas'),
    path('receta_crear/', views.receta_crear, name='receta_crear'),
    path('consejeros/', views.lista_consejeros, name='lista_consejeros'),


    #SISTEMA CORREO AUTOMATICO Y OLVIDO DE CONTRASEÑA
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html", email_template_name="reset_password_email.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),

    #CRUD CONSEJEROS
    path('Administracion/', Home_Administracion),
    path('Administracion/Consejeros/listado/', consejero_listado, name='listado_consejeros'),
    path('Administracion/Consejeros/insertar/', consejero_insertar, name='consejero_insertar'),
    path('Administracion/Consejeros/borrar/<int:idconsejeros>/', borrar_consejero),
    path('Administracion/Consejeros/actualizar/<int:idconsejeros>/', consejero_actualizar),
    path('mostrar-imagen-grande/<path:imagen_url>/', views.mostrar_imagen_grande, name='mostrar_imagen_grande'),

    #CRUD ROLES
    path('Administracion/Roles/listado/', listado_roles, name='listado_roles'),
    path('Administracion/Roles/insertar/', insertar_roles, name='insertar_roles'),
    path('Administracion/Roles/borrar/<int:idroles>', borrar_rol),
    path('Administracion/Roles/actualizar/<int:idroles>', actualizar_rol),
    #FIN CRUD ROLES

    #DIETAS DISPONIBLES - CALENDARIO
    path('salud-nutricion/dietas/', lista_dietas, name='lista_dietas'),
    path('dietas/buscar/', buscar_dietas, name='buscar_dietas'),
]