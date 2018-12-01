from django.urls import path
from apps.Productos.views import index, invproductos, invcategorias, viewProductos, viewCategoria, viewVenta, nuevoRegistro, editarRegistro, eliminarRegistro, nuevoRegistroc, editarRegistroc, eliminarRegistroc, ventas, agregarCarrito, pagar
app_name = 'Productos';
urlpatterns = [
	path('', viewProductos.as_view()),
	path('index', viewProductos.as_view()),
	path('invproductos', viewProductos.as_view(), name="listaProductos"),
	path('invcategorias', viewCategoria.as_view(), name="listaCategorias"),
	path('nuevoRegistro', nuevoRegistro, name="nuevoRegistro"),
	path('editarRegistro/<id>', editarRegistro, name="editarRegistro"),
	path('eliminarRegistro/<id>', eliminarRegistro, name="eliminarRegistro"),
	path('nuevoRegistroc', nuevoRegistroc, name="nuevoRegistroc"),
	path('editarRegistroc/<id>', editarRegistroc, name="editarRegistroc"),
 	path('eliminarRegistroc/<id>', eliminarRegistroc, name="eliminarRegistroc"),
 	path('ventas', viewVenta.as_view(), name="ventas"),
 	path('agregarCarrito/<id>', agregarCarrito, name = "agregarCarrito"),
 	path('pagar', pagar, name = "pagar"),


]