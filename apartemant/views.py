from urllib import request

from django.shortcuts import render

from apartemant.models import Apartment


def show_apartment(request):
    apartemants = Apartment.objects.all()

    return render(request, 'apartment.html', {'apartemants': apartemants})


def filter_reserve_apartment():
    apartemant_status = Apartment.objects.filter(apartmentStatuses='inactive')
    return render(request, 'apartment.html', {'apartemants': apartemant_status})


def add_apartment(request, data):
    apartment1 = Apartment(
        price=data['price'],
        tenant=data['tenant'],
        rent_price=data['rent_price'],
        owner=data['owner'],
        floor=data['floor'],
        floor_count=data['floor_count'],
        room_count=data['room_count'],
        area=data['area'],
        mortgage_price=data['mortgage_price'],
        phone=data['phone'],
        apartmentStatuses=data['apartmentStatuses'],
        phoneStatuses=data['phoneStatuses'],
        address_aprtment=data['address_aprtment'])
    Apartment.save(apartment1)
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def delete_apartment(request, a_id):
    # get(pk=this_object_id)
    apartemant = Apartment.objects.get(pk=a_id)
    Apartment.delete(apartemant)


def update_apartment(request, data, a_id):
    Apartment.objects.filter(pk=a_id).update(
        price=data['price'],
        tenant=data['tenant'],
        rent_price=data['rent_price'],
        owner=data['owner'],
        floor=data['floor'],
        floor_count=data['floor_count'],
        room_count=data['room_count'],
        area=data['area'],
        mortgage_price=data['mortgage_price'],
        phone=data['phone'],
        apartmentStatuses=data['apartmentStatuses'],
        phoneStatuses=data['phoneStatuses'],
        address_aprtment=data['address_aprtment']
        )
    # apartemant = Apartment.objects.get(pk=a_id)
    # apartemant.price = data['price']
    # apartemant.price = data['price'],
    # apartemant.tenant = data['tenant'],
    # apartemant.rent_price = data['rent_price'],
    # apartemant.owner = data['owner'],
    # apartemant.floor = data['floor'],
    # apartemant.floor_count = data['floor_count'],
    # apartemant.room_count = data['room_count'],
    # apartemant.area = data['area'],
    # apartemant.mortgage_price = data['mortgage_price'],
    # apartemant.phone = data['phone'],
    # apartemant.apartmentStatuses = data['apartmentStatuses'],
    # apartemant.phoneStatuses = data['phoneStatuses'],
    # apartemant.address_aprtment = data['address_aprtment']
    # Apartment.save(apartemant)
