from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.show_apartment,name= 'show_apartment'),
    path('add/',views.add_apartment,name='add_apartment' ),
]