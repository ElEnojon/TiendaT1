from django import forms
from apps.Productos.models import Productos

class ProductoForm(forms.ModelForm):
	class Meta:

		model = Productos

		fields = [

			'nombreProducto',
			'descripcion',
			'costo',
			'disponibilidad',
			'categoria',
			'Existencias'

		]

		labels = {

			'nombreProducto' : 'Nombre del producto',
			'descripcion' : 'Descripcion del producto',
			'costo' : 'Costo',
			'disponibilidad' : 'Disponibilidad',
			'categoria' : 'Categoria',
			'Existencias' : 'Existencias'
		}

		widgets = {

			'nombreProducto':forms.TextInput(attrs={'class' : 'form-control'}),
			'descripcion':forms.TextInput(attrs={'class' : 'form-control'}),
			'costo':forms.TextInput(attrs={'class' : 'form-control'}),
			'disponibilidad':forms.TextInput(attrs={'class' : 'form-control'}),
			'categoria':forms.TextInput(attrs={'class' : 'form-control'}),

		}


class VentaProductoForm(forms.ModelForm):

	class Meta:
		model = Productos
		fields = [
			'nombreProducto',
			'costo',
			'disponibilidad',
			'Existencias'

		]
		labels = {
			'nombreProducto' : 'Nombre',
			'costo' : 'Costo',
			'disponibilidad' : 'Disponible',
			'Existencias' : 'Existencias'
		}
		widgets = {
			'nombreProducto':forms.TextInput(attrs = {'class':'form-control','id':'nombreProducto', 'disabled':'true'}),
			'costo':forms.TextInput(attrs = {'class':'form-control','id':'costo','disabled':'true'}),
			'disponibilidad':forms.TextInput(attrs = {'class':'form-control','id':'disponibilidad','disabled':'true'}),
			'Existencias':forms.TextInput(attrs = {'class':'form-control','id':'Existencias','disabled':'true'}),

		}

