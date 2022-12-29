# آپارتمان
# مشخصه ها: قیمت - مالک - مستاجر - تعداد اتاق - متراژ - طبقه -
# تعداد طبقات - آدرس - تلفن فعال/غیرفعال - مبلغ رهن - مبلغ اجاره -
# مبلغ فروش - فروشی/استیجاری - پارکینگ - آسانسور - استخر
# Create your models here.
from datetime import datetime

from django.db import models
# from django.contrib.auth.hashers import check_password

# Create your models here.
from django.db import models

# Create your models here.
from address.models import Address
from user.models import User


# from django.contrib.auth.hashers import check_password


class Apartment(models.Model):
    apartment_status = [
        ('rent', 'Rent'),
        ('sell', 'Sell'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    phone_status = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    price = models.CharField(max_length=25, null=False)
    owner = models.ForeignKey(User, verbose_name='owner_id', related_name='owner_user',
                              on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(User, verbose_name='tenant_id', related_name='User',
                               on_delete=models.CASCADE, null=True)
    floor = models.IntegerField()
    floor_count = models.IntegerField()
    room_count = models.IntegerField()
    area = models.IntegerField()
    phone = models.CharField(max_length=11)
    rent_price = models.CharField(max_length=25)
    mortgage_price = models.CharField(max_length=25)
    sell_price = models.CharField(max_length=25)
    apartmentStatuses = models.CharField(choices=apartment_status, max_length=15)
    phoneStatuses = models.CharField(choices=phone_status, max_length=15)
    address_aprtment = models.ForeignKey(Address, verbose_name='apertment_id', related_name='Address',
                                         on_delete=models.CASCADE, null=True)
    start_date = models.DateField(default=datetime.now(),null=True)
    end_date = models.DateField(default=datetime.now(),null=True)

    def __str__(self):
        return str(self.floor) + ":" + self.owner.username + ":" + self.apartmentStatuses + ":" + self.price
