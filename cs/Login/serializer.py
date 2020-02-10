# --------Agregar librerias Framework -------
from rest_framework import routers, serializers, viewsets

# -------Agregar modelos ---------
from Login.models import Example2
# nombre de app. recurso .. llamado

class Example2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields= ('__all__')

