# Generated by Django 4.1.4 on 2022-12-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('avenue_name', models.CharField(max_length=50)),
                ('plate', models.CharField(max_length=3)),
                ('zipCode', models.CharField(max_length=10)),
            ],
        ),
    ]