from django.urls import path

from  . import views

app_name= "carro"

urlpatterns = [
   
    path('agregar/<int:producto_id>', views.agregar_producto, name="agregar"),

    path('eliminar/<int:producto_id>', views.eliminar_producto, name="eliminar"),

    path('restar/<int:producto_id>', views.restar_producto, name="restar"),

    path('limpiar/', views.limpiar_carroproducto, name="limpiar"),

    path('activar-desactivar/', views.activar_desactivar_carro, name='activar_desactivar_carro'),

    path('mostrar-carro/', views.mostrar_carro, name='mostrar_carro'),


]
