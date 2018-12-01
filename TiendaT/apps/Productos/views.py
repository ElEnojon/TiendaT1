from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from apps.Productos.models import Productos, Categoria
from apps.Productos.forms import ProductoForm, VentaProductoForm
from apps.Productos.formc import  CategoriaForm

def index(request):
	return HttpResponse("Esta es la respuesta");


def invproductos(request):

	contexto ={
		'Productos': Productos.objects.all()
	}

	return render(request, 'tablas/productos.html', contexto)


def invcategorias(request):
	contexto = {
		'Productos': Categoria.objects.all()

	}

	return render(request, 'tablas/categorias.html', contexto)


def ventas(request):
	contexto = {
	'Productos': Productos.objects.all()
	}

	return render(request, 'tablas/ventas.html', contexto)



class viewProductos(ListView):
	model = Productos
	template_name = 'tablas/productos.html'

class viewCategoria(ListView):
	model = Categoria
	template_name = 'tablas/categorias.html'

class viewVenta(ListView):
	model = Productos
	template_name = 'tablas/ventas.html'



def nuevoRegistro(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaProductos') #listaProductos viene del name"" en path en urls.py
	else:
		form = ProductoForm()
	return render(request, 'tablas/prodForm.html', {'form':form});

def editarRegistro(request, id):
	Producto = Productos.objects.get(id=id)
	if request.method == 'GET':
		form = ProductoForm(instance = Producto) #el nombre de la instance viene del model en forms.py
	else:
		form = ProductoForm(request.POST, instance = Producto)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaProductos')
	return render(request, 'tablas/prodForm.html', {'form':form})

def eliminarRegistro(request, id):
	Producto = Productos.objects.get(id=id).delete()
	return redirect('Productos:listaProductos')

#Formulario





# Formulario categorias
def nuevoRegistroc(request):
	if request.method == 'POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaCategorias')
	else:
		form = CategoriaForm()
	return render(request, 'tablas/catForm.html', {'form':form});

def editarRegistroc(request, id):
	Categoria2 = Categoria.objects.get(id=id)
	if request.method == 'GET':
		form = CategoriaForm(instance = Categoria2) #el nombre de la instance viene del model en forms.py
	else:
		form = CategoriaForm(request.POST, instance = Categoria2)
		if form.is_valid():
			form.save()
		return redirect ('Productos:listaCategorias')
	return render(request, 'tablas/catForm.html', {'form':form})

def eliminarRegistroc(request, id):
	Categoria2 = Categoria.objects.get(id=id).delete()
	return redirect('Productos:listaCategorias')

# # #Formulario

def agregarCarrito(request, id):
	producto = Productos.objects.get(id=id)
	if (request.method == 'GET'):
		form = VentaProductoForm(instance = producto)
	return render(request, 'tablas/ventaFormulario.html', {'form': form})

def pagar(request):
	return redirect('Productos:ventas')