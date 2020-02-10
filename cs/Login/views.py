from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from decouple import config
#necesario vistas 
from django.shortcuts import get_list_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
#necesario vistas

from Login.models import Example2
from Login.serializer import Example2Serializers


class ExampleList2(APIView):
    #get
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        #many =true si aplica el retorno
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        pass
    #     serializer = Example2Serializers(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         datas = serializer.get_unique_for_date_validators
    #         return Response(datas)
    #     return Response(serializer.errors, status=status.HTT)

class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                'request': request, 
                                                }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })