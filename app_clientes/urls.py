from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('clientes/<int:id_cliente>/', views.ver_cliente, name='ver_cliente'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
]