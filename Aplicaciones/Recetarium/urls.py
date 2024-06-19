from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import Home_Administracion, bienvenido, actualizar_rol, borrar_consejero, borrar_rol, buscar_dietas, insertar_roles, lista_dietas, lista_recetas, buscar_recetas, listado_roles, receta_crear, lista_consejeros, ver_recetas_usuarios, plan_nutricional, Not_Found, bmi_calculator, salud_nutricion, registro_usuario , loginusuarios, usuario , informacion

from .views import actualizar_rol, borrar_rol, buscar_dietas, crud_listado_ingredientes, insertar_roles, lista_dietas, lista_recetas, buscar_recetas, listado_roles, lista_consejeros, ver_recetas_usuarios, plan_nutricional, Not_Found, bmi_calculator, salud_nutricion, loginusuarios
 

urlpatterns = [
    # INDEX
    path('', views.index, name='index'),
    # Bienvenido
    path('Bienvenido', views.bienvenido, name='bienvenido'),
    # Crear o ver recetas ( Apartado Usuario )
    path('eleccion-ver-crear-receta/', views.crear_elegir_receta, name='crear_elegir_receta'),
    #recuperacion de contraseña
    path('recuperacion-de-contraseña/', views.olvido_contraseña, name='olvido_contraseña'),
    #soporte tecnico
    path('soporte-tecnico/', views.soporte_tecnico, name='soporte_tecnico'),
    # Calculadora IMC de salud 
    path('calculadora-salud/', views.bmi_calculator, name='bmi_calculator'),
    # Lista de Recetas 
    path('recetas/', views.lista_recetas, name='lista_recetas'),
    # visualizacion de cada una de las recetas  o ( recetas ampliadas )
    path('detalle_receta/<int:id_receta>/', views.detalle_receta, name='detalle_receta'),
    # Glosario
    path('informacion', views.informacion, name='informacion'),

    path('buscar/', views.buscar_recetas, name='buscar_recetas'),
    # Crear Recetas
    path('receta_crear/', views.receta_crear, name='receta_crear'),
    # Pagina de los consejeros visibles 
    path('consejeros/', views.lista_consejeros, name='lista_consejeros'),
    # Plan Nutricional Calendario Personalizable
    path('plan/', views.plan_nutricional, name='plan_nutricional'),
    # Pagina no funciona ( not found )
    path('not_found/', views.Not_Found, name='not_found'),
    # Salud y nutricion ( Apartado de Usuario )
    path('salud_nutricion', views.salud_nutricion, name='salud_nutricion'),

    # Generador
    
    # SISTEMA CORREO AUTOMATICO Y OLVIDO DE CONTRASEÑA
    path('reset/password_reset/', auth_views.PasswordResetView.as_view(template_name='mail/password_reset_form.html'), name='password_reset'),
    path('reset/password_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name='mail/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='mail/reset.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='mail/password_reset_complete.html'), name='password_reset_complete'),

    # CRUD CONSEJEROS
    path('administracion/', views.dashboard , name='home_administracion'),
    path('administracion/consejeros/listado/', views.listar_consejeros, name='listar_consejeros'),
    path('administracion/consejeros/insertar/', views.crear_consejero, name='crear_consejero'),
    path('administracion/consejeros/actualizar/<int:pk>', views.actualizar_consejero, name='actualizar_consejero'),
    path('administracion/consejeros/borrar/<int:pk>', views.borrar_consejero, name='borrar_consejero'),
    path('administracion/consejeros/ver/<int:id_consejero>/', views.mostrar_imagen_grande, name='mostrar_imagen_grande'),

    #CRUD RECETAS
    path('administracion/recetas/listado/', views.listar_recetas, name='listar_recetas'),
    path('administracion/recetas/insertar/', views.crear_receta, name='crear_receta'),
    path('administracion/recetas/actualizar/<int:pk>/', views.actualizar_receta, name='actualizar_receta'),
    path('administracion/recetas/borrar/<int:pk>', views.borrar_receta, name='borrar_receta'),
    path('administracion/recetas/ver/<int:receta_id>/', views.ver_recetas, name='ver_receta'),
    path('ver-imagen/<int:id_receta>/', views.ver_imagen, name='ver_imagen'),

    #CRUD DIETAS
    path('administracion/dietas/listado/', views.listar_dietas, name='listar_dietas'),
    path('administracion/dietas/insertar/', views.crear_dietas, name='crear_dietas'),
    path('administracion/dietas/borrar/<int:pk>', views.borrar_dietas, name='borrar_dietas'),
    path('administracion/dietas/actualizar/<int:pk>/', views.actualizar_dietas, name='actualizar_dietas'),
    path('administracion/dietas/ver/<int:dieta_id>/', views.ver_dietas, name='ver_dietas'),
    path('administracion/dietas/ver_imagen/<int:id_dieta_c>/', views.mostrar_imagen_grande_dieta, name='mostrar_imagen_grande_dieta'),

    #CRUD INGREDIENTES
    path('administracion/ingredientes/listado', crud_listado_ingredientes, name='listado_ingredientes'),
    path('administracion/ingredientes/insertar/', views.crear_ingrediente, name='crear_ingrediente'),
    path('administracion/ingredientes/actualizar/<int:pk>/', views.actualizar_ingrediente, name='actualizar_ingrediente'),
    path('administracion/ingredientes/borrar/<int:pk>/', views.borrar_ingrediente, name='borrar_ingrediente'),
    path('administracion/ingredientes/ver/<int:ingrediente_id>/', views.ver_ingrediente, name='ver_ingrediente'),

    # CRUD ROLES
    path('administracion/roles/listado/', listado_roles, name='listado_roles'),
    path('administracion/roles/insertar/', insertar_roles, name='insertar_roles'),
    path('administracion/roles/borrar/<int:idroles>/', borrar_rol, name='borrar_rol'),
    path('administracion/roles/actualizar/<int:idroles>/', actualizar_rol, name='actualizar_rol'),

    # DIETAS DISPONIBLES - CALENDARIO
    path('salud-nutricion/dietas/', lista_dietas, name='lista_dietas'),
    path('dietas/buscar/', buscar_dietas, name='buscar_dietas'),
    
    # USUARIO LOGIN REGISTER , LOGOUT , USUARIO
    path('Usuarios/registro/', registro_usuario , name='registro_usuario'),
    path('Usuarios/login/', loginusuarios, name='login_usuario'),
    path('Usuarios/usuario/', usuario, name='usuario'),

    path('salud-nutricion/dietas/dieta=<int:id_dieta_c>/', views.detalle_dietas, name='detalle_dietas'),

    #FIN DIETAS DISPONIBLES - CALENDARIO

    #VER RECETAS USUARIOS
    path('recetas/<int:usuario_id>/tus_recetas/', ver_recetas_usuarios, name="ver_recetas_usuarios"),
    #FIN VER RECETAS USUARIOS

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)