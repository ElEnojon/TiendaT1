from django.contrib import admin

from apps.Productos.models import Productos, Categoria

admin.site.register(Productos)
admin.site.register(Categoria)
