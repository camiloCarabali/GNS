from rest_framework import serializers
from ApiApp.models import Requests

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = ('id', 'date', 'method', 'consult', 'dataReturn')
