# Generated by Django 4.1.4 on 2022-12-29 08:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_house_end_date_alter_house_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 11, 50, 42, 375053), null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 11, 50, 42, 375053), null=True),
        ),
    ]
