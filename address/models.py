from django.db import models


# from django.contrib.auth.hashers import check_password

# Create your models here.
# مشخصه ها: نام شهر - نام خیابان - شماره پلاک - کدپستی
class Address(models.Model):
    city_name = models.CharField(max_length=50, null=False)
    avenue_name = models.CharField(max_length=50, null=False)
    plate = models.CharField(max_length=3, null=False)
    zipCode = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.city_name + ":" + self.avenue_name + ":" + \
               self.zipCode + ":" + self.plate
