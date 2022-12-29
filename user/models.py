from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# : نام - نام خانوادگی - آدرس ایمیل - کدملی - شماره تلفن - عکس

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    national_code = models.CharField(max_length=10, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+919198989'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)  # validators should be a list
    # phone_number = models.CharField(max_length=10)
    email = models.EmailField(null=False, unique=True)
    image=models.ImageField(upload_to="images", max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=8)




    class Meta:
        verbose_name = 'کاربران'

    def __str__(self):
        return self.first_name+":" + self.last_name

