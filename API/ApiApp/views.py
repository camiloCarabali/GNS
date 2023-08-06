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
    """
       Muestra los usuarios obtenidos desde una API externa y registra la consulta en la base de datos.

       Si el método de la solicitud es GET, realiza una solicitud a una API externa, registra los detalles de la consulta
       en la base de datos y devuelve los datos de los usuarios obtenidos en formato JSON.

       Parámetros:
           request (HttpRequest): La solicitud HTTP recibida.

       Retorna:
           JsonResponse: Una respuesta JSON que contiene los datos de los usuarios obtenidos desde la API externa.

    """

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
    """
        Muestra las publicaciones obtenidas desde una API externa y registra la consulta en la base de datos.

        Si el método de la solicitud es GET, realiza una solicitud a una API externa que contiene las publicaciones,
        registra los detalles de la consulta en la base de datos y devuelve los datos de las publicaciones obtenidas
        en formato JSON.

        Parámetros:
            request (HttpRequest): La solicitud HTTP recibida.

        Retorna:
            JsonResponse: Una respuesta JSON que contiene los datos de las publicaciones obtenidas desde la API externa.

    """
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
    """
        Busca las fotos asociadas a un usuario específico mediante su ID y registra la consulta en la base de datos.

        Si el método de la solicitud es GET, realiza dos solicitudes a API externas para obtener las listas de álbumes y
        fotos asociadas al usuario especificado por su ID. Luego, registra los detalles de la consulta en la base de datos
        y devuelve los datos de las fotos obtenidas en formato JSON.

        Parámetros:
            request (HttpRequest): La solicitud HTTP recibida.
            id (int, opcional): El ID del usuario para el cual se busca las fotos asociadas.

        Retorna:
            JsonResponse: Una respuesta JSON que contiene los datos de las fotos obtenidas desde las API externas.

    """

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
    """
        Muestra todas las solicitudes almacenadas en la base de datos.

        Si el método de la solicitud es GET, recupera todas las instancias del modelo Requests almacenadas en la base de datos,
        las serializa utilizando el RequestSerializer y devuelve los datos de las solicitudes en formato JSON.

        Parámetros:
            request (HttpRequest): La solicitud HTTP recibida.

        Retorna:
            JsonResponse: Una respuesta JSON que contiene los datos de todas las solicitudes almacenadas en la base de datos.

    """
    if request.method == 'GET':
        requests = Requests.objects.all()
        requests_serializers = RequestSerializer(requests, many=True)
        return JsonResponse(requests_serializers.data, safe=False)


@csrf_exempt
def modifyRequests(request):
    """
        Modifica una solicitud existente en la base de datos.

        Si el método de la solicitud es PUT, se espera que los datos de la solicitud a modificar se envíen en formato JSON
        en el cuerpo de la solicitud. Luego, busca la solicitud en la base de datos mediante su ID y actualiza sus campos
        con los nuevos datos proporcionados. Devuelve un mensaje de éxito en formato JSON si la modificación es exitosa.

        Nota:
        - Se debe habilitar el decorador '@csrf_exempt' para evitar problemas de CSRF al permitir solicitudes PUT desde fuera
          del sitio web.

        Parámetros:
            request (HttpRequest): La solicitud HTTP recibida.

        Retorna:
            JsonResponse: Una respuesta JSON que indica si la solicitud fue modificada con éxito.

    """

    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        request = Requests.objects.get(id=request_data['id'])
        request_serializers = RequestSerializer(request, data=request_data)
        if request_serializers.is_valid():
            request_serializers.save()
            return JsonResponse("Registro Modificado", safe=False)


@csrf_exempt
def deleteRequests(request, id=0):
    """
       Elimina una solicitud existente de la base de datos.

       Si el método de la solicitud es DELETE, busca la solicitud en la base de datos mediante su ID y la elimina.
       Devuelve un mensaje de éxito en formato JSON si la eliminación es exitosa.

       Nota:
       - Se debe habilitar el decorador '@csrf_exempt' para evitar problemas de CSRF al permitir solicitudes DELETE desde fuera
         del sitio web.

       Parámetros:
           request (HttpRequest): La solicitud HTTP recibida.
           id (int, opcional): El ID de la solicitud que se desea eliminar. Por defecto es 0.

       Retorna:
           JsonResponse: Una respuesta JSON que indica si la solicitud fue eliminada con éxito.

       """
    if request.method == 'DELETE':
        request = Requests.objects.get(id=id)
        request.delete()
        return JsonResponse("Registro Eliminado", safe=False)
