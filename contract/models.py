from datetime import datetime

from django.db import models

from apartemant.models import Apartment
from home.models import House
from shop.models import Shop


class Contract(models.Model):
    shop = models.ForeignKey(Shop, verbose_name='shop_id', related_name='shopContract',
                             on_delete=models.CASCADE, null=True)
    house = models.ForeignKey(House, verbose_name='house_id', related_name='houseContract',
                              on_delete=models.CASCADE, null=True)
    appartment = models.ForeignKey(Apartment, verbose_name='appartment_id', related_name='appartmentContract',
                                   on_delete=models.CASCADE, null=True)
    start_date = models.DateField(default=datetime.now(), null=True)
    end_date = models.DateField(default=datetime.now(), null=True)
