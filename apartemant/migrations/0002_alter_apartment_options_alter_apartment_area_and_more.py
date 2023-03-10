# Generated by Django 4.1.4 on 2022-12-29 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('apartemant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='area',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='floor_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='mortgage_price',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner_user', to='user.user', verbose_name='owner_id'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='rent_price',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='room_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='sell_price',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='user.user', verbose_name='tenant_id'),
        ),
    ]
