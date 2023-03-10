# Generated by Django 4.1.4 on 2022-12-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartemant', '0002_alter_apartment_options_alter_apartment_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='end_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='apartmentStatuses',
            field=models.CharField(choices=[('rent', 'Rent'), ('sell', 'Sell'), ('active', 'Active'), ('inactive', 'Inactive')], max_length=15),
        ),
    ]
