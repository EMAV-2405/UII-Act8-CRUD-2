from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Cliente

# Listar clientes
def index(request): # <-- ¡Asegúrate de que esta función esté presente y se llame 'index'!
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

# Ver detalle de un cliente
def ver_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    return render(request, 'ver_cliente.html', {'cliente': cliente})

# Agregar cliente
def agregar_cliente(request):
    if request.method == 'POST':
        id_cliente = request.POST['id_cliente']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo_electronico = request.POST['correo_electronico']
        telefono = request.POST.get('telefono', '')

        Cliente.objects.create(
            id_cliente=id_cliente,
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            telefono=telefono,
        )
        return redirect('inicio')
    return render(request, 'agregar_cliente.html')

# Editar cliente
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        cliente.id_cliente = request.POST['id_cliente']
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.correo_electronico = request.POST['correo_electronico']
        cliente.telefono = request.POST.get('telefono', '')
        cliente.save()
        return redirect('inicio')
    return render(request, 'editar_cliente.html', {'cliente': cliente})

# Borrar cliente
def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('inicio')
    return render(request, 'borrar_cliente.html', {'cliente': cliente})