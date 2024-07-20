from django.urls import path, include
from AppProyectoPython.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('index/', home, name="index"),
    path('cliente/', cliente, name="cliente"),
    path('cotizacion/', cotizacion, name="cotizacion"),
    path('producto/', producto, name="producto"),
    path('acercade/', acercade, name="acercade"),
    
    #Formularios
    path('clienteForm/', clienteForm, name="clienteForm"),
    path('cotizacionForm/', cotizacionForm, name="cotizacionForm"),
    path('productoForm/', productoForm, name="productoForm"),
    
    
    #path('buscarProducto/', buscarProducto, name="buscarProducto"),
    
    path('clienteUpdate/<id_cliente>', clienteUpdate, name="clienteUpdate"),
    path('cotizacionUpdate/<id_cotizacion>', cotizacionUpdate, name="cotizacionUpdate"),
    path('productoUpdate/<id_producto>', productoUpdate, name="productoUpdate"),
    
    path('clienteDelete/<id_cliente>', clienteDelete, name="clienteDelete"),
    path('cotizacionDelete/<id_cotizacion>', cotizacionDelete, name="cotizacionDelete"),
    path('productoDelete/<id_producto>', productoDelete, name="productoDelete"),

    
    path('fichaproducto/', FichaProductoList.as_view(), name="fichaproducto"),
    path('fichaproductoCreate/', FichaProductoCreate.as_view(), name="fichaproductoCreate"),
    path('fichaproductoUpdate/<int:pk>', FichaProductoUpdate.as_view(), name="fichaproductoUpdate"),
    path('fichaproductoDelete/<int:pk>', FichaProductoDelete.as_view(), name="fichaproductoDelete"),
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name = "entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    
    #Editar perfiles y avatares
    path('perfil/', editarPerfil, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),

    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

]       