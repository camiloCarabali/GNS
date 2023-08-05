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
        endpoint_1 = f"https://jsonplaceholder.typicode.com/albums?userId={id}"
        endpoint_2 = "https://jsonplaceholder.typicode.com/photos?albumId="
        timestamp = datetime.now()

        response_1 = requests.get(endpoint_1)
        response_data_1 = response_1.json()

        list_1 = []
        list_2 = []

        for obj in response_data_1:
            if obj["userId"] == int(id):
                list_1.append(obj["id"])

        for id_ in list_1:
            url = endpoint_2 + str(id_)
            response_2 = requests.get(url)
            response_data_2 = response_2.json()
            list_2.extend(response_data_2)

        json_data = list_2

        api_log = Requests(
            date=timestamp.date(),
            method=method,
            consult=endpoint_2,
            dataReturn=json_data
        )
        api_log.save()

        return JsonResponse(json_data, safe=False)
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
