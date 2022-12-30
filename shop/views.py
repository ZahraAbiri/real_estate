from urllib import request

from django.shortcuts import render

from shop.models import Shop


def show_shop(request):
    apartemants = Shop.objects.all()

    # return render(request, 'apartment.html', {'apartemants': apartemants})todo


def filter_reserve_apartment():
    apartemant_status = Shop.objects.filter(apartmentStatuses='inactive')
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def add_apartment(request, data):
    shop = Shop(
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
    Shop.save(shop)
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def delete_apartment(request, a_id):
    # get(pk=this_object_id)
    apartemant = Shop.objects.get(pk=a_id)
    Shop.delete(apartemant)


def update_apartment(request, data, a_id):
    Shop.objects.filter(pk=a_id).update(
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

