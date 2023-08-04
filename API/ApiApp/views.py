from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ApiApp.models import Requests
from ApiApp.serializers import RequestSerializer
import requests
from datetime import datetime


# Create your views here.

@csrf_exempt
def showUsers(request):
    if request.method == 'GET':
        method = "GET"
        endpoint = "https://jsonplaceholder.typicode.com/users"
        timestamp = datetime.now()

        response = requests.get(endpoint)
        response_data = response.json()

        api_log = Requests(
            date=timestamp.date(),
            method=method,
            consult=endpoint,
            dataReturn=response_data
        )
        api_log.save()

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def showPosts(request):
    if request.method == 'GET':
        method = "GET"
        endpoint = "https://jsonplaceholder.typicode.com/posts"
        timestamp = datetime.now()

        response = requests.get(endpoint)
        response_data = response.json()

        api_log = Requests(
            date=timestamp.date(),
            method=method,
            consult=endpoint,
            dataReturn=response_data
        )
        api_log.save()

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def searchPhotosUsers(request, id=0):
    if request.method == 'GET':
        method = "GET"
        endpoint = f"https://jsonplaceholder.typicode.com/photos?albumId={id}"
        timestamp = datetime.now()

        response = requests.get(endpoint)
        response_data = response.json()

        api_log = Requests(
            date=timestamp.date(),
            method=method,
            consult=endpoint,
            dataReturn=response_data
        )
        api_log.save()

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def showRequests(request):
    if request.method == 'GET':
        requests = Requests.objects.all()
        requests_serializers = RequestSerializer(requests, many=True)
        return JsonResponse(requests_serializers.data, safe=False)


@csrf_exempt
def modifyRequests(request):
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        request = Requests.objects.get(id=request_data['id'])
        request_serializers = RequestSerializer(request, data=request_data)
        if request_serializers.is_valid():
            request_serializers.save()
            return JsonResponse("Registro Modificado", safe=False)


@csrf_exempt
def deleteRequests(request, id=0):
    if request.method == 'DELETE':
        request = Requests.objects.get(id=id)
        request.delete()
        return JsonResponse("Registro Eliminado", safe=False)
