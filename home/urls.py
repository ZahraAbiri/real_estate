from django.urls import path
from . import views

urlpatterns = [
    path('seeAll/',views.show_house),
]