from django.shortcuts import render

# Create your views here.

from decouple import config
#necesario vistas 
from django.shortcuts import get_list_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
#necesario vistas

from Profile.models import Profile,Ciudad,Genero,Ocupacion,Estado,EstadoCivil
from Profile.serializer import ProfileSerializers,CiudadSerializers,GeneroSerializers,OcupacionSerializers,EstadoCivilSerializers,EstadoSerializers


class ProfileList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoCivilList(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset =EstadoCivil.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)