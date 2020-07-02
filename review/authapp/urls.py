from django.urls import path,include
from .import views

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('abi/', views.Api_objects.as_view()),
    path('abi/<int:pk>/', views.Api_objects_details.as_view()),
]