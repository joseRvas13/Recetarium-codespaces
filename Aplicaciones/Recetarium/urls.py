from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name="index"),
    path('crear-elegir-receta/', views.crear_elegir_receta),
    path('recuperacion-de-contraseña/', views.olvido_contraseña, name="olvido_contraseña"),
    path('salud-nutricion/', views.salud_nutricion, name="salud_nutricion"),
    path('calculadora-salud/', views.calculadora_salud, name="calculadora_salud"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),

    #SISTEMA CORREO AUTOMATICO Y OLVIDO DE CONTRASEÑA
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html", email_template_name="reset_password_email.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"), name="password_reset_complete"),
]