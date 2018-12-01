from django import forms
from apps.Productos.models import Categoria

class CategoriaForm(forms.ModelForm):
	class Meta:
	
		model = Categoria

		fields = [

			'nombreCat'
		]


		labels = {
		'nombreCat' : 'Nombre de la categoria'
		}

		widgets = {

		'nombreCat':forms.TextInput(attrs={'class' : 'form-control'})
		}