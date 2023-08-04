from django.urls import path
from CountryApp import views

urlpatterns = [
    path('country/', views.showCountry),
    path('createCountry/', views.createCountry),
    path('modifyCountry/', views.modifyCountry),
    path('deleteCountry/<id>', views.deleteCountry),
]
