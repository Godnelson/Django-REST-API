from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import *
from .models import *


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CategoriaViewSet(request, pk=''):

    if pk == '':
        if request.method == 'GET':
            queryset = Categoria.objects.all()
            serializer_class = CategoriaSerializer(queryset, many=True)
            return Response(serializer_class.data)
        elif request.method == 'POST':
            serializer = CategoriaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            queryset = Categoria.objects.get(id=pk)
        except Categoria.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = CategoriaSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            serializer = CategoriaSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def FilmesViewSet(request, pk=''):
    if pk == '':
        if request.method == 'GET':
            queryset = Filmes.objects.all()
            serializer_class = FilmesSerializer(queryset, context={"request": 
                      request}, many=True)
            return Response(serializer_class.data)
        elif request.method == 'POST':
            serializer = FilmesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            queryset = Filmes.objects.get(id=pk)
        except Filmes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = FilmesSerializer(queryset, context={"request": 
                      request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            serializer = FilmesSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AssinaturaViewSet(request, pk=''):

    if pk == '':
        if request.method == 'GET':
            queryset = Assinatura.objects.all()
            serializer_class = AssinaturaSerializer(queryset, many=True)
            return Response(serializer_class.data)
        elif request.method == 'POST':
            serializer = AssinaturaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            queryset = Assinatura.objects.get(id=pk)
        except Assinatura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = AssinaturaSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PUT':
            serializer = AssinaturaSerializer(queryset, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def UsuariosViewSet(request, pk=''):
    if pk == '':
        if request.method == 'GET':
            queryset = Usuarios.objects.all()
            serializer = UsuariosSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = UsuariosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            queryset = Usuarios.objects.get(id=pk)
        except Usuarios.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = UsuariosSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = UsuariosSerializer(queryset, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def FavoritosViewSet(request, pk=''):
    if pk == '':
        if request.method == 'GET':
            queryset = Favoritos.objects.all()
            serializer = FavoritosSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = FavoritosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            queryset = Favoritos.objects.get(id=pk)
        except Favoritos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serializer = FavoritosSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = FavoritosSerializer(queryset, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)