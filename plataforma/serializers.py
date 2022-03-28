from .models import *
from rest_framework import serializers

class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = '__all__'
    
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AssinaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assinatura
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class FavoritosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoritos
        fields = '__all__'

