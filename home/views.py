from django.shortcuts import render

from home.models import House


def show_house(request):
    apartemants=House.objects.all()

    return render(request, 'apartment.html', {'apartemants':apartemants})
