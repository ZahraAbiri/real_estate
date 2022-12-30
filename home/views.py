from urllib import request

from django.shortcuts import render

from home.models import House


def show_house(request):
    house=House.objects.all()

    # return render(request, 'apartment.html', {'apartemants':apartemants})todo




def filter_reserve_house():
    apartemant_status = House.objects.filter(apartmentStatuses='inactive')
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def add_house(request, data):
    house = House(
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
    House.save(house)
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def delete_house(request, a_id):
    # get(pk=this_object_id)
    house = House.objects.get(pk=a_id)
    House.delete(house)


def update_house(request, data, a_id):
    House.objects.filter(pk=a_id).update(
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
