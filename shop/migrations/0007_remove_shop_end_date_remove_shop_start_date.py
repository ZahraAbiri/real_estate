# Generated by Django 4.1.4 on 2022-12-30 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_shop_end_date_alter_shop_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='start_date',
        ),
    ]
