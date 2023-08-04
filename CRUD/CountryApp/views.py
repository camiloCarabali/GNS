from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CountryApp.models import Country
from CountryApp.serializers import CountrySerializer


# Create your views here.

@csrf_exempt
def showCountry(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        country_serializers = CountrySerializer(countries, many=True)
        return JsonResponse(country_serializers.data, safe=False)


@csrf_exempt
def createCountry(request):
    if request.method == 'POST':
        country_data = JSONParser().parse(request)
        country_serializers = CountrySerializer(data=country_data)
        if country_serializers.is_valid():
            country_data.save()
            return JsonResponse("Added Country", safe=False)
        return JsonResponse("Failed to add country", safe=False)


@csrf_exempt
def modifyCountry(request):
    if request.method == 'PUT':
        country_data = JSONParser().parse(request)
        country = Country.objects.get(id=country_data['id'])
        country_serializers = CountrySerializer(country, data=country_data)
        if country_serializers.is_valid():
            country_serializers.save()
            return JsonResponse("Modified Country", safe=False)
        return JsonResponse("Failed to change country", safe=False)


@csrf_exempt
def deleteCountry(request, id=0):
    if request.method == 'DELETE':
        country = Country.objects.get(id=id)
        country.delete()
        return JsonResponse("country removed", safe=False)
