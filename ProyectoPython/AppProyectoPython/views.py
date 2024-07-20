from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from AppProyectoPython.models import *
from AppProyectoPython.forms import * 

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Aqui se crean las funciones para las vistas. Son HTML renderizados por Django
# Crear variable contexto para identificar cada modelo en las etiquetas DTL de los html
def home(request):
    return render(request, "entidades/index.html")

def acercade(request):
    return render(request, "entidades/acercade.html")


# CLIENTES
@login_required
def cliente(request):
    contexto = {"cliente": Cliente.objects.all()}
    return render(request, "entidades/cliente.html", contexto)

@login_required
def clienteForm (request):
    if request.method == "POST":
        #Aqui se resuelve el formulario con datos, validandolos
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_correo = miForm.cleaned_data.get("correo")
            cliente_telefono = miForm.cleaned_data.get("telefono")
            #se crea el objeto cliente
            cliente = Cliente(nombre = cliente_nombre, correo = cliente_correo, telefono = cliente_telefono) 
            #Guardamos los datos en la BD
            cliente.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = { "cliente": Cliente.objects.all()}
            return render(request, "entidades/cliente.html", contexto)
    else:
        #Creamos un formulario vacío para que el usuario lo complete 
        
        miForm = ClienteForm()
        #Renderizamos y enviamos request al html que mostrará el form como diccionario
        return render(request, "entidades/clienteForm.html", {"form": miForm})

@login_required        
def clienteUpdate(request, id_cliente): #Función de actualización del registro de la DB. Se le entrega el ID para identificar el registro
    #Se hace el match de id  
    cliente = Cliente.objects.get(id=id_cliente) 
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre = miForm.cleaned_data.get("nombre")
            cliente.correo = miForm.cleaned_data.get("correo")
            cliente.telefono = miForm.cleaned_data.get("telefono")
            #Guardamos los datos en la BD
            cliente.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = { "cliente": Cliente.objects.all()}
            return render(request, "entidades/cliente.html", contexto)
    else:
        miForm = ClienteForm(initial={"nombre":cliente.nombre, "correo": cliente.correo, "telefono": cliente.telefono})
    return  render(request, "entidades/clienteForm.html", {"form":miForm})

@login_required
def clienteDelete(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    contexto = {"cliente": Cliente.objects.all()}
    return render(request, "entidades/cliente.html", contexto)
    

# COTIZACIONES
@login_required
def cotizacion(request):
    contexto = {"cotizacion": Cotizacion.objects.all()}
    return render(request, "entidades/cotizacion.html", contexto)
@login_required
def cotizacionForm (request):
    if request.method == "POST":
        #Aqui se resuelve el formulario con datos, validandolos
        miForm = CotizacionForm(request.POST)
        if miForm.is_valid():
            cotizacion_detalle = miForm.cleaned_data.get("detalle")
            cotizacion_mayorista = miForm.cleaned_data.get("mayorista")
            #se crea el objeto 
            cotizacion = Cotizacion(detalle = cotizacion_detalle, mayorista = cotizacion_mayorista) 
            #Guardamos los datos en la BD
            cotizacion.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = {"cotizacion": Cotizacion.objects.all()}
            return render(request, "entidades/cotizacion.html", contexto)
    else:
        #Creamos un formulario vacío para que el usuario lo complete 
        
        miForm = CotizacionForm()
        #Renderizamos y enviamos request al html que mostrará el form como diccionario
        return render(request, "entidades/cotizacionForm.html", {"form": miForm})
@login_required    
def cotizacionUpdate(request, id_cotizacion): #Función de actualización del registro de la DB. Se le entrega el ID para identificar el registro
    #Se hace el match de id  
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    if request.method == "POST":
        miForm = CotizacionForm(request.POST)
        if miForm.is_valid():
            cotizacion.detalle = miForm.cleaned_data.get("detalle")
            cotizacion.mayorista = miForm.cleaned_data.get("mayorista")
            #Guardamos los datos en la BD
            cotizacion.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = { "cotizacion": Cotizacion.objects.all()}
            return render(request, "entidades/cotizacion.html", contexto)
    else:
        miForm = CotizacionForm(initial={"detalle":cotizacion.detalle, "mayorista": cotizacion.mayorista})
    return  render(request, "entidades/cotizacionForm.html", {"form":miForm})
@login_required
def cotizacionDelete(request, id_cotizacion):
    cotizacion = Cotizacion.objects.get(id=id_cotizacion)
    cotizacion.delete()
    contexto = {"cotizacion": Cotizacion.objects.all()}
    return render(request, "entidades/cotizacion.html", contexto)
    
#PRODUCTOS

def producto(request):
    contexto = {"producto": Producto.objects.all()}
    return render(request, "entidades/producto.html", contexto)

@login_required    
def productoForm (request):
    if request.method == "POST":
        #Aqui se resuelve el formulario con datos, validandolos
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombreProducto")
            producto_marca = miForm.cleaned_data.get("marca")
            producto_stock = miForm.cleaned_data.get("stock")
            producto_precio =  miForm.cleaned_data.get("precio")
            producto_url = miForm.cleaned_data.get("url")

            #se crea el objeto 
            producto = Producto(nombreProducto = producto_nombre, marca = producto_marca, stock = producto_stock, precio = producto_precio, url = producto_url) 
            #Guardamos los datos en la BD
            producto.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = {"producto": Producto.objects.all()}
            return render(request, "entidades/producto.html", contexto)
    else:
        #Creamos un formulario vacío para que el usuario lo complete 
        
        miForm = ProductoForm()
        #Renderizamos y enviamos request al html que mostrará el form como diccionario
        return render(request, "entidades/productoForm.html", {"form": miForm})
    
    
#def buscarProducto(request):
#    return render(request, "entidades/buscar.html")
@login_required
def productoUpdate(request, id_producto): #Función de actualización del registro de la DB. Se le entrega el ID para identificar el registro
    #Se hace el match de id  
    producto = Producto.objects.get(id=id_producto)
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.nombreProducto = miForm.cleaned_data.get("nombreProducto")
            producto.marca = miForm.cleaned_data.get("marca")
            producto.stock = miForm.cleaned_data.get("stock")
            producto.precio = miForm.cleaned_data.get("precio")
            producto.url = miForm.cleaned_data.get("url")
            #Guardamos los datos en la BD
            producto.save()
            #Vamos a crear un contexto para redirigir a la página donde se muestran los datos de la BD de clientes
            contexto = {"producto": Producto.objects.all()}
            return render(request, "entidades/producto.html", contexto)
    else:
        miForm = ProductoForm(initial={"nombreProducto":producto.nombreProducto, "marca": producto.marca, "stock":producto.stock, "precio": producto.precio, "url": producto.url})
    return  render(request, "entidades/productoForm.html", {"form":miForm})

@login_required
def productoDelete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    producto.delete()
    contexto = {"producto": Producto.objects.all()}
    return render(request, "entidades/producto.html", contexto)

# FICHA DE PRODUCTO (HERENCIA)
class FichaProductoList(LoginRequiredMixin, ListView):
    model = FichaProducto
    template_name ='entidades/fichaproducto_list.html'
    
class FichaProductoCreate(LoginRequiredMixin, CreateView):
    model = FichaProducto
    fields = ["titulo", "descripcion", "especificacion"]
    success_url = reverse_lazy("fichaproducto")
    template_name ='entidades/fichaproducto_form.html'
    
class FichaProductoUpdate(LoginRequiredMixin, UpdateView):
    model = FichaProducto
    fields = ["titulo", "descripcion", "especificacion"]
    success_url = reverse_lazy("fichaproducto")
    template_name ='entidades/fichaproducto_form.html'
    
class FichaProductoDelete(LoginRequiredMixin, DeleteView):
    model = FichaProducto
    success_url = reverse_lazy("fichaproducto")
    template_name ='entidades/fichaproducto_confirm_delete.html'
    
    
#LOGIN/ LOGOUT/ REGISTATION

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            #Buscar avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"]= avatar
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = RegistroForm()
        
    return render(request, "entidades/registro.html", {"form": miForm})


# EDITAR PERFILES Y AVATARES
@login_required

def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView): 
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")
    
@login_required    
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #Se borran los avatares antiguos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar = Avatar(user=usuario, imagen=imagen)       
            avatar.save()
            
            #enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})