from django.shortcuts import render

from address.models import Address


def add_address(request, data):
    address = Address(
        city_name=data['city_name'],
        avenue_name=data['avenue_name'],
        plate=data['plate'],
        zipCode=data['zipCode'])
    Address.save(address)
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def delete_address(request, a_id):
    # get(pk=this_object_id)
    apartemant = Address.objects.get(pk=a_id)
    Address.delete(apartemant)


def update_address(request, data, a_id):
    Address.objects.filter(pk=a_id).update(
        city_name=data['city_name'],
        avenue_name=data['avenue_name'],
        plate=data['plate'],
        zipCode=data['zipCode']
        )

