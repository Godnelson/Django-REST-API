from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Filmes)
admin.site.register(Categoria)
admin.site.register(Usuarios)
admin.site.register(Favoritos)
admin.site.register(Assinatura)