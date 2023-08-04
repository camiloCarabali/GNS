from django.urls import path
from ApiApp import views

urlpatterns = [
    path('showUsers/', views.showUsers),
    path('showPosts/', views.showPosts),
    path('searchPhotosUsers/<id>', views.searchPhotosUsers),
    path('showRequests/', views.showRequests),
    path('modifyRequests/', views.modifyRequests),
    path('deleteRequests/<id>', views.deleteRequests)
]
