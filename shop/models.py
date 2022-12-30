from datetime import datetime

from django.db import models
# مشخصه ها: قیمت -  مالک - مستاجر - متراژ - آدرس - تلفن فعال/غیرفعال
# - مبلغ رهن - مبلغ اجاره - مبلغ فروش - فروشی/استیجاری
from django.db import models
# from django.contrib.auth.hashers import check_password

# Create your models here.
from address.models import Address
from user.models import User


class Shop(models.Model):
    shop_status = [
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
    owner = models.ForeignKey(User, verbose_name='owner_id', related_name='shop_owner_user',
                              on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(User, verbose_name='tenant_id', related_name='shop_tenant_user',
                               on_delete=models.CASCADE, null=True)
    area = models.IntegerField()
    phone = models.CharField(max_length=11)
    rent_price = models.CharField(max_length=25)
    mortgage_price = models.CharField(max_length=25)
    sell_price = models.CharField(max_length=25)
    shopStatuses = models.CharField(choices=shop_status, max_length=15)
    phoneStatuses = models.CharField(choices=phone_status, max_length=15)
    address_aprtment = models.ForeignKey(Address, verbose_name='apertment_id', related_name='shop_address',
                                         on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.owner.username + ":" + self.shopStatuses + ":" + self.price
