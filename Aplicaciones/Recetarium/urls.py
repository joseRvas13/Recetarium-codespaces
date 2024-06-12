from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    Home_Administracion, actualizar_rol, borrar_consejero, borrar_rol,
    buscar_dietas, consejero_actualizar, consejero_insertar, consejero_listado,
    insertar_roles, lista_dietas, lista_recetas, buscar_recetas, listado_roles,
    receta_crear, lista_consejeros, plan_nutricional, Not_Found,
    bmi_calculator, salud_nutricion, usuarioinsertar, loginusuarios
)

urlpatterns = [
    path('', views.index, name='index'),
    path('eleccion-ver-crear-receta/', views.crear_elegir_receta, name='crear_elegir_receta'),
    path('recuperacion-de-contraseña/', views.olvido_contraseña, name='olvido_contraseña'),
    path('soporte-tecnico/', views.soporte_tecnico, name='soporte_tecnico'),
    path('calculadora-salud/', views.bmi_calculator, name='bmi_calculator'),
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    path('detalle_receta/<int:id_receta>/', views.detalle_receta, name='detalle_receta'),
    path('invalid_page/', views.invalid_page, name='invalid_page'),
    path('buscar/', views.buscar_recetas, name='buscar_recetas'),
    path('receta_crear/', views.receta_crear, name='receta_crear'),
    path('consejeros/', views.lista_consejeros, name='lista_consejeros'),
    path('plan/', views.plan_nutricional, name='plan_nutricional'),
    path('not_found/', views.Not_Found, name='not_found'),
    path('salud_nutricion', views.salud_nutricion, name='salud_nutricion'),

    # SISTEMA CORREO AUTOMATICO Y OLVIDO DE CONTRASEÑA
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='reset_password.html', email_template_name='reset_password_email.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),

    # CRUD CONSEJEROS
    path('administracion/', Home_Administracion, name='home_administracion'),
    path('administracion/consejeros/listado/', consejero_listado, name='listado_consejeros'),
    path('administracion/consejeros/insertar/', consejero_insertar, name='consejero_insertar'),
    path('administracion/consejeros/borrar/<int:idconsejeros>/', borrar_consejero, name='borrar_consejero'),
    path('administracion/consejeros/actualizar/<int:idconsejeros>/', consejero_actualizar, name='actualizar_consejero'),
    path('mostrar-imagen-grande/<path:imagen_url>/', views.mostrar_imagen_grande, name='mostrar_imagen_grande'),

    # CRUD ROLES
    path('administracion/roles/listado/', listado_roles, name='listado_roles'),
    path('administracion/roles/insertar/', insertar_roles, name='insertar_roles'),
    path('administracion/roles/borrar/<int:idroles>/', borrar_rol, name='borrar_rol'),
    path('administracion/roles/actualizar/<int:idroles>/', actualizar_rol, name='actualizar_rol'),

    # DIETAS DISPONIBLES - CALENDARIO
    path('salud-nutricion/dietas/', lista_dietas, name='lista_dietas'),
    path('dietas/buscar/', buscar_dietas, name='buscar_dietas'),
    
    # USUARIO LOGIN REGISTER , LOGOUT
     path('Usuarios/insertar/', usuarioinsertar, name='insertar_usuario'),
    path('Usuarios/login/', loginusuarios, name='login_usuario'),
]