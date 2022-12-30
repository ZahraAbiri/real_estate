from django.shortcuts import render

from user.models import User


def add_user(request, data):
    user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        national_code=data['national_code'],
        phone_number=data['phone_number'],
        email=data['email'],
        username=data['username'],
        password=data['password'])
    User.save(user)
    # return render(request, 'apartment.html', {'apartemants': apartemant_status})todo


def delete_apartment(request, a_id):
    user = User.objects.get(pk=a_id)
    User.delete(user)


def update_apartment(request, data, a_id):
    User.objects.filter(pk=a_id).update(
        first_name=data['first_name'],
        last_name=data['last_name'],
        national_code=data['national_code'],
        phone_number=data['phone_number'],
        email=data['email'],
        username=data['username'],
        password=data['password']
        )
    