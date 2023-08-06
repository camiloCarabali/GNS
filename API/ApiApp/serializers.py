from rest_framework import serializers
from ApiApp.models import Requests


class RequestSerializer(serializers.ModelSerializer):
    """
        Serializador para el modelo de solicitudes (Requests).

        Este serializador permite convertir instancias del modelo Requests en formato JSON y viceversa.

        Atributos:
            model (Model): La clase del modelo que se va a serializar.
            fields (tuple): Una tupla que especifica los campos del modelo que se incluirán en la serialización.

    """

    class Meta:
        model = Requests
        fields = ('id', 'date', 'method', 'consult', 'dataReturn')
