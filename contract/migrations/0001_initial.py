# Generated by Django 4.1.4 on 2022-12-29 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0005_alter_shop_end_date_alter_shop_start_date'),
        ('home', '0006_alter_house_end_date_alter_house_start_date'),
        ('apartemant', '0007_alter_apartment_end_date_alter_apartment_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime(2022, 12, 29, 12, 1, 44, 683259), null=True)),
                ('end_date', models.DateField(default=datetime.datetime(2022, 12, 29, 12, 1, 44, 683259), null=True)),
                ('appartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appartmentContract', to='apartemant.apartment', verbose_name='appartment_id')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='houseContract', to='home.house', verbose_name='house_id')),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopContract', to='shop.shop', verbose_name='shop_id')),
            ],
        ),
    ]