from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('categoria/', views.CategoriaViewSet),
    path('categoria/<pk>', views.CategoriaViewSet),
    path('filmes/', views.FilmesViewSet),
    path('filmes/<pk>', views.FilmesViewSet),
    path('assinatura/', views.AssinaturaViewSet),
    path('assinatura/<pk>', views.AssinaturaViewSet),
    path('usuarios/', views.UsuariosViewSet),
    path('usuarios/<pk>', views.UsuariosViewSet),
    path('favoritos/', views.FavoritosViewSet),
    path('favoritos/<pk>', views.FavoritosViewSet),
]