# Generated by Django 4.1.4 on 2022-12-29 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('national_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+919198989'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'کاربر',
            },
        ),
    ]
