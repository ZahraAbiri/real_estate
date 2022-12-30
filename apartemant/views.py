from django.http import HttpResponse
from django.shortcuts import render

from apartemant.models import Apartment


def show_apartment(request):
    apartemants=Apartment.objects.all()

    return render(request, 'apartment.html', {'apartemants':apartemants})



